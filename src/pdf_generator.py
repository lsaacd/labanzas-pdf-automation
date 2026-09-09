"""
PDF Generation Engine for Alabanzas Letras.
Implements the visual design specification:
- Page: US Letter (612 x 792 pt)
- Title: DancingScript-Bold (26 pt)
- Body: Economica-Regular (13 pt, uppercase)
- Alignment: 100% Centered horizontal on X = 306 pt
- Dynamic 1-page Auto-Fit algorithm
"""

import os
from typing import Optional
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont

from .models import Song


class LetraPDFGenerator:
    def __init__(self, fonts_dir: Optional[str] = None):
        if fonts_dir is None:
            base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
            candidate = os.path.join(base_dir, "[04] ASSETS", "fonts")
            if os.path.exists(candidate):
                fonts_dir = candidate
            else:
                fonts_dir = os.path.join(base_dir, "fonts")
        
        self.fonts_dir = fonts_dir
        self._register_fonts()

    def _register_fonts(self):
        dancing_path = os.path.join(self.fonts_dir, "DancingScript-Bold.ttf")
        economica_reg = os.path.join(self.fonts_dir, "Economica-Regular.ttf")
        economica_bold = os.path.join(self.fonts_dir, "Economica-Bold.ttf")

        if os.path.exists(dancing_path):
            pdfmetrics.registerFont(TTFont("DancingScript-Bold", dancing_path))
        if os.path.exists(economica_reg):
            pdfmetrics.registerFont(TTFont("Economica-Regular", economica_reg))
        if os.path.exists(economica_bold):
            pdfmetrics.registerFont(TTFont("Economica-Bold", economica_bold))

    def generate(self, song: Song, output_pdf_path: str) -> str:
        """
        Renders the song into a pixel-perfect 1-page PDF matching the church standard.
        """
        os.makedirs(os.path.dirname(os.path.abspath(output_pdf_path)), exist_ok=True)
        c = canvas.Canvas(output_pdf_path, pagesize=letter)
        width, height = letter  # 612 x 792 pt
        center_x = width / 2.0

        # Collect all renderable items for width and height calculations
        items = []
        for sec in song.sections:
            if sec.heading:
                items.append(("Economica-Bold", sec.heading.strip()))
            for line in sec.lines:
                clean_line = line.strip()
                if clean_line:
                    items.append(("Economica-Regular", clean_line))

        total_items = len(items)
        total_gaps = max(1, len(song.sections))

        # Dynamic Auto-Fit calculation:
        # Fills the majority of the page comfortably while respecting margins
        available_h = height - 150.0
        units = total_items + (total_gaps * 0.45)
        ideal_line_height = available_h / units
        target_font = ideal_line_height / 1.38
        target_font = min(15.5, max(11.5, target_font))

        # Horizontal safety check: ensure no line breaks or exceeds printable width
        max_allowed_w = width - 72.0  # at least 36pt (0.5 in) margin on each side
        max_w = max(pdfmetrics.stringWidth(text, fn, target_font) for fn, text in items)
        if max_w > max_allowed_w:
            target_font = target_font * (max_allowed_w / max_w)

        font_size = round(target_font, 1)
        line_height = font_size * 1.38
        section_gap = line_height * 1.45

        # Calculate total content height
        total_content_height = (total_items * line_height) + (total_gaps * (section_gap - line_height))

        # Balanced vertical positioning
        # Enhanced title font size for high visibility and calligraphic elegance
        title_font_size = 36 if font_size >= 14.5 else 33
        title_y = height - 68.0
        lyrics_start_y = title_y - 54.0

        expected_bottom = lyrics_start_y - total_content_height
        if expected_bottom > 85.0:
            offset = min(25.0, (expected_bottom - 85.0) / 2.0)
            title_y -= offset
            lyrics_start_y -= offset

        # 1. Draw Title
        c.setFont("DancingScript-Bold", title_font_size)
        c.drawCentredString(center_x, title_y, song.title)

        # 2. Draw Sections and Lines
        c.setFont("Economica-Regular", font_size)
        cur_y = lyrics_start_y

        for sec in song.sections:
            # Section Heading (Numbers, CORO:, PUENTE:, FINAL:)
            if sec.heading:
                c.setFont("Economica-Bold", font_size)
                c.drawCentredString(center_x, cur_y, sec.heading.strip())
                cur_y -= line_height
                c.setFont("Economica-Regular", font_size)

            # Section Lyric Lines
            for line in sec.lines:
                clean_line = line.strip()
                if clean_line:
                    c.drawCentredString(center_x, cur_y, clean_line)
                    cur_y -= line_height

            # Inter-section gap
            cur_y -= (section_gap - line_height)

        c.showPage()
        c.save()
        return output_pdf_path
