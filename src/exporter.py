"""
Exporter module to output Alabanzas data to JSON, Markdown, and TXT.
"""

import os
import json
from .models import Song


class SongExporter:
    @staticmethod
    def save_json(song: Song, output_path: str) -> str:
        os.makedirs(os.path.dirname(os.path.abspath(output_path)), exist_ok=True)
        with open(output_path, "w", encoding="utf-8") as f:
            json.dump(song.to_dict(), f, indent=2, ensure_ascii=False)
        return output_path

    @staticmethod
    def save_markdown(song: Song, output_path: str) -> str:
        os.makedirs(os.path.dirname(os.path.abspath(output_path)), exist_ok=True)
        with open(output_path, "w", encoding="utf-8") as f:
            f.write(song.to_markdown())
        return output_path

    @staticmethod
    def save_text(song: Song, output_path: str) -> str:
        os.makedirs(os.path.dirname(os.path.abspath(output_path)), exist_ok=True)
        with open(output_path, "w", encoding="utf-8") as f:
            f.write(song.to_text())
        return output_path
