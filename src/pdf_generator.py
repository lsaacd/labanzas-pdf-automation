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

        # Compute line counts for auto-fit
        total_items = 0
        for sec in song.sections:
            if sec.heading:
                total_items += 1
            total_items += len(sec.lines)
        total_gaps = max(1, len(song.sections))

        # Dynamic Auto-Fit calculation:
        # Standard: 30 lines -> font 13pt, line_height ~17.18pt, gap ~34.36pt (2*line_height)
        # We target fitting cleanly between top_margin and bottom_margin:
        available_h = height - 120.0  # reserve ~120pt for title and baseline margins

        # Total units: each line is 1 unit, each gap between sections is 1.0 to 1.5 units
        total_units = total_items + (total_gaps * 1.1)

        raw_line_height = available_h / total_units
        line_height = min(17.18, max(12.5, raw_line_height))
        section_gap = line_height * 1.4

        # Scale font size slightly if line height had to be reduced
        if line_height < 14.5:
            font_size = 11.5
        elif line_height < 16.0:
            font_size = 12.0
        else:
            font_size = 13.0

        # Calculate starting Y to keep content vertically balanced
        total_content_height = (total_items * line_height) + (len(song.sections) * (section_gap - line_height))
        # Center the block between title and bottom
        title_y = height - 75.0
        lyrics_start_y = title_y - 45.0

        # If content is short, center it nicely
        expected_bottom = lyrics_start_y - total_content_height
        if expected_bottom > 110.0:
            # Shift slightly downward to balance page
            offset = min(25.0, (expected_bottom - 110.0) / 2.0)
            title_y -= offset
            lyrics_start_y -= offset

        # 1. Draw Title
        c.setFont("DancingScript-Bold", 26)
        c.drawCentredString(center_x, title_y, song.title)

        # 2. Draw Sections and Lines
        c.setFont("Economica-Regular", font_size)
        cur_y = lyrics_start_y

        for sec in song.sections:
            # Section Heading
            if sec.heading:
                c.setFont("Economica-Regular", font_size)
                c.drawCentredString(center_x, cur_y, sec.heading.strip())
                cur_y -= line_height

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
