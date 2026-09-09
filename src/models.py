"""
Data models and schema definitions for Alabanzas Choral to Lyrics automation.
IDDV El Buen Pastor - Coro Unido Filadelfia
"""

from dataclasses import dataclass, field, asdict
from typing import List, Optional
import json


@dataclass
class SongSection:
    type: str  # "CORO", "ESTROFA", "PUENTE", "FINAL"
    heading: str  # e.g. "CORO:", "1.", "2.", "FINAL:"
    lines: List[str] = field(default_factory=list)

    def to_dict(self):
        return {
            "type": self.type,
            "heading": self.heading,
            "lines": self.lines
        }

    @classmethod
    def from_dict(cls, data: dict):
        return cls(
            type=data.get("type", "ESTROFA"),
            heading=data.get("heading", ""),
            lines=data.get("lines", [])
        )


@dataclass
class Song:
    title: str
    author: Optional[str] = None
    hymn_number: Optional[str] = None
    event_info: Optional[str] = None
    sections: List[SongSection] = field(default_factory=list)

    def to_dict(self):
        return {
            "title": self.title,
            "author": self.author,
            "hymn_number": self.hymn_number,
            "event_info": self.event_info,
            "sections": [s.to_dict() for s in self.sections]
        }

    @classmethod
    def from_dict(cls, data: dict):
        sections = [SongSection.from_dict(s) for s in data.get("sections", [])]
        return cls(
            title=data.get("title", ""),
            author=data.get("author"),
            hymn_number=data.get("hymn_number"),
            event_info=data.get("event_info"),
            sections=sections
        )

    def to_markdown(self) -> str:
        lines = [f"# {self.title}\n"]
        if self.author:
            lines.append(f"**Autor:** {self.author}\n")
        if self.hymn_number:
            lines.append(f"**Número:** {self.hymn_number}\n")
        if self.event_info:
            lines.append(f"*{self.event_info}*\n")
        lines.append("---\n")

        for sec in self.sections:
            if sec.heading:
                lines.append(f"### {sec.heading}\n")
            for line in sec.lines:
                lines.append(f"{line}  ")
            lines.append("\n")

        return "\n".join(lines)

    def to_text(self) -> str:
        lines = [self.title, ""]
        for sec in self.sections:
            if sec.heading:
                lines.append(sec.heading)
            for line in sec.lines:
                lines.append(line)
            lines.append("")
        return "\n".join(lines).strip()
