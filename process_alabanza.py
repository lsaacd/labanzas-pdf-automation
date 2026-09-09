"""
CLI and Automation Runner for Alabanzas: Partitura to Letra.
IDDV El Buen Pastor - Coro Unido Filadelfia
"""

import os
import sys
import json
import argparse
import fitz

from src.models import Song
from src.pdf_generator import LetraPDFGenerator
from src.exporter import SongExporter


def process_song_file(json_file_path: str, output_base_dir: str, generate_png_preview: bool = True):
    with open(json_file_path, "r", encoding="utf-8") as f:
        data = json.load(f)

    song = Song.from_dict(data)
    clean_title = song.title.replace("¡", "").replace("!", "").replace("¿", "").replace("?", "").strip()
    
    # Categorized output directories
    pdf_dir = os.path.join(output_base_dir, "[01] PDF")
    md_dir = os.path.join(output_base_dir, "[02] MARKDOWN")
    txt_dir = os.path.join(output_base_dir, "[03] TEXT")
    preview_dir = os.path.join(output_base_dir, "[04] PREVIEWS")

    for d in [pdf_dir, md_dir, txt_dir, preview_dir]:
        os.makedirs(d, exist_ok=True)

    # 1. Output PDF
    pdf_path = os.path.join(pdf_dir, f"{clean_title} Letra.pdf")
    generator = LetraPDFGenerator()
    generator.generate(song, pdf_path)
    print(f"  [PDF OK] -> {pdf_path}")

    # 2. Output Markdown
    md_path = os.path.join(md_dir, f"{clean_title} Letra.md")
    SongExporter.save_markdown(song, md_path)
    print(f"  [MD  OK] -> {md_path}")

    # 3. Output Plain Text
    txt_path = os.path.join(txt_dir, f"{clean_title} Letra.txt")
    SongExporter.save_text(song, txt_path)
    print(f"  [TXT OK] -> {txt_path}")

    # 4. PNG Preview for instant verification
    if generate_png_preview:
        doc = fitz.open(pdf_path)
        png_path = os.path.join(preview_dir, f"{clean_title} Letra_preview.png")
        doc[0].get_pixmap(dpi=150).save(png_path)
        print(f"  [IMG OK] -> {png_path}")

    return pdf_path


def main():
    parser = argparse.ArgumentParser(description="Alabanzas Choral to Lyrics Automation Runner")
    parser.add_argument("--song", type=str, help="Name or prefix of the song to process (e.g. 'yo_soy_hijo_de_dios')")
    parser.add_argument("--all", action="store_true", help="Process all songs in [02] SONGS DATA/")
    parser.add_argument("--list", action="store_true", help="List all available songs")
    args = parser.parse_args()

    base_dir = os.path.dirname(os.path.abspath(__file__))
    
    # Path resolution for organized folders
    songs_dir = os.path.join(base_dir, "[02] SONGS DATA")
    if not os.path.exists(songs_dir):
        songs_dir = os.path.join(base_dir, "songs_data")
        
    output_dir = os.path.join(base_dir, "[03] OUTPUT LETRAS")
    if not os.path.exists(output_dir):
        output_dir = os.path.join(base_dir, "output_letras")

    if args.list:
        print("Canciones disponibles en [02] SONGS DATA/:")
        for f in os.listdir(songs_dir):
            if f.endswith(".json"):
                print(f"  - {f}")
        return

    songs_to_process = []
    if args.all or (not args.song and not args.all and not args.list):
        for f in os.listdir(songs_dir):
            if f.endswith(".json"):
                songs_to_process.append(os.path.join(songs_dir, f))
    elif args.song:
        target = args.song.lower()
        for f in os.listdir(songs_dir):
            if f.endswith(".json") and target in f.lower():
                songs_to_process.append(os.path.join(songs_dir, f))

    if not songs_to_process:
        print("No se encontraron canciones para procesar.")
        return

    print(f"\nIniciando procesamiento de {len(songs_to_process)} alabanza(s)...")
    for song_file in songs_to_process:
        print(f"\nProcesando: {os.path.basename(song_file)}")
        process_song_file(song_file, output_dir)

    print("\nProcesamiento completado con éxito.")


if __name__ == "__main__":
    main()
