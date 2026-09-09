"""
Compile unified songbook (Cancionero) PDF:
Preserves original Cover (Page 1) and Index (Page 2),
followed by the 9 converted 1-page lyric sheets in exact index order.
"""

import os
try:
    import pymupdf as fitz  # PyMuPDF
except ImportError:
    import fitz

def prepare_cover_with_vector_logo(partitura_doc, svg_path):
    """
    Replaces the rasterized, noisy /Im1 logo on Cover (Page 0)
    with the clean, ultra-high resolution vector SVG logo.
    """
    p = partitura_doc[0]

    # 1. Remove /Im1 Do from page content streams
    for xref in p.get_contents():
        stream_str = partitura_doc.xref_stream(xref).decode("latin1", errors="ignore")
        if "/Im1 Do" in stream_str:
            stream_str = stream_str.replace("/Im1 Do", "       ")
            partitura_doc.update_stream(xref, stream_str.encode("latin1"))

    # 2. Parse SVG, inline CSS fill classes, convert to vector PDF
    with open(svg_path, "r", encoding="utf-8") as f:
        svg_content = f.read()

    styles = dict(re.findall(r"\.(st\d+)\s*\{\s*fill:\s*([^;]+);?\s*\}", svg_content))
    for k, v in styles.items():
        svg_content = re.sub(rf'class=["\']{k}["\']', f'fill="{v}"', svg_content)

    doc_svg = fitz.open(stream=svg_content.encode("utf-8"), filetype="svg")
    svg_pdf = fitz.open("pdf", doc_svg.convert_to_pdf())

    # 3. Target rect on original page (where Im1 was originally located)
    rect_logo = fitz.Rect(358.3882, 112.7911, 439.0653, 228.9661)
    p.show_pdf_page(rect_logo, svg_pdf, 0)
    print("  [OK] Logo rasterizado reemplazado por logo vectorial SVG nítido.")

def prepare_index_with_corrected_title(partitura_doc, font_path):
    """
    Fixes grammar mistake ('Alabnzas' -> 'Alabanzas') and vertical overlap
    between 'Coro Maranatha' and 'Índice de Alabanzas' on Page 2 (index),
    maintaining the exact original font OpenSauceOne-Regular.
    """
    p = partitura_doc[1]

    # 1. Remove /Fm17 Do from page 1 content stream so the misspelled overlapping text is not drawn
    for xref in p.get_contents():
        stream_str = partitura_doc.xref_stream(xref).decode("latin1", errors="ignore")
        if "/Fm17 Do" in stream_str:
            stream_str = stream_str.replace("/Fm17 Do", "        ")
            partitura_doc.update_stream(xref, stream_str.encode("latin1"))

    # 2. Re-insert the corrected text with proper vertical spacing and the exact font
    p.insert_text(
        fitz.Point(161.38, 218.0),
        "Índice de Alabanzas",
        fontfile=font_path,
        fontsize=42.042,
        color=(0, 0, 0)
    )
    print("  [OK] Título de Índice corregido ('Índice de Alabanzas') y espaciado sin colisiones.")

def compile_maranatha_songbook():
    base_dir = os.path.dirname(os.path.abspath(__file__))
    input_partituras = os.path.join(base_dir, "[01] INPUT PARTITURAS", "Coro Maranatha - El ADN del Reino (Partituras).pdf")
    svg_logo_path = os.path.join(base_dir, "[04] ASSETS", "og_ebp.svg")
    if not os.path.exists(svg_logo_path):
        svg_logo_path = os.path.join(base_dir, "og_ebp.svg")

    index_font_path = os.path.join(base_dir, "[04] ASSETS", "fonts", "OpenSauceOne-Regular.ttf")
    if not os.path.exists(index_font_path):
        index_font_path = os.path.join(base_dir, "extracted_opensauce.ttf")

    pdf_letras_dir = os.path.join(base_dir, "[03] OUTPUT LETRAS", "[01] PDF")
    output_pdf_path = os.path.join(pdf_letras_dir, "Coro Maranatha - El ADN del Reino (Letras).pdf")
    previews_dir = os.path.join(base_dir, "[03] OUTPUT LETRAS", "[04] PREVIEWS")

    ordered_song_filenames = [
        "A Tu Nombre Gloria Letra.pdf",
        "Al Santo Señor Letra.pdf",
        "Aleluya Letra.pdf",
        "Como No Agradecer Letra.pdf",
        "Elias Letra.pdf",
        "Estar Siempre Con El Letra.pdf",
        "Cambiaste Mi Vida Letra.pdf",
        "No te Imaginas Cuánto te Amo Letra.pdf",
        "Viene Pronto Letra.pdf"
    ]

    print("Iniciando compilación del Cancionero 'El ADN del Reino'...")
    final_doc = fitz.open()

    # 1. Insert original Cover (Page 1) and Index (Page 2) scaled to standard Letter size (612 x 792 pt)
    print(f"  Extrayendo y escalando Portada e Índice a tamaño Carta de: {input_partituras}")
    partitura_doc = fitz.open(input_partituras)

    # Replace raster logo on cover with vector SVG
    if os.path.exists(svg_logo_path):
        prepare_cover_with_vector_logo(partitura_doc, svg_logo_path)

    # Fix grammar mistake and overlap on Index page (Page 2)
    if os.path.exists(index_font_path):
        prepare_index_with_corrected_title(partitura_doc, index_font_path)

    letter_rect = fitz.Rect(0, 0, 612, 792)

    for page_idx in [0, 1]:
        page_carta = final_doc.new_page(width=612, height=792)
        page_carta.show_pdf_page(letter_rect, partitura_doc, page_idx, keep_proportion=False)
    print("  [OK] Portada e Índice insertados y estandarizados a tamaño Carta (Páginas 1 y 2).")

    # 2. Insert 9 standardized 1-page lyric PDFs
    for idx, filename in enumerate(ordered_song_filenames, start=1):
        file_path = os.path.join(pdf_letras_dir, filename)
        if not os.path.exists(file_path):
            # Try alternate accent encoding if needed
            for f in os.listdir(pdf_letras_dir):
                if f.lower() == filename.lower():
                    file_path = os.path.join(pdf_letras_dir, f)
                    break
        
        song_doc = fitz.open(file_path)
        final_doc.insert_pdf(song_doc, from_page=0, to_page=0)
        print(f"  [OK] Canción {idx}: {filename} insertada (Página {idx + 2}).")

    # Save final compiled PDF
    final_doc.save(output_pdf_path)
    print(f"\n[ÉXITO] Cancionero completo compilado: {output_pdf_path}")
    print(f"Total de páginas: {len(final_doc)}")

    # Generate preview of the compiled songbook (Page 1 Cover, Page 2 Index, and Page 3 first song)
    for p in range(min(4, len(final_doc))):
        prev_img_path = os.path.join(previews_dir, f"Himnario_Maranatha_pag_{p+1}.png")
        final_doc[p].get_pixmap(dpi=150).save(prev_img_path)
        print(f"  [PREVIEW OK] -> {prev_img_path}")

    return output_pdf_path

if __name__ == "__main__":
    compile_maranatha_songbook()
