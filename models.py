"""
Dev 128 Fall 2025 Section 27802
Rob Ranf
Final Project
GitHub Repo: https://github.com/rlr524/anime-to-manga-risuto

models.py - The model classes for the program's three objects: Anime, Manga, and Genre
"""

from dataclasses import dataclass

@dataclass
class Anime:
    id: int = 0
    title: str = ""
    year: str = ""
    seasons: str = ""
    rating: float = 0.0
    owned: str = ""
    notes: str = ""


@dataclass
class Manga:
    id: int = 0
    title: str = ""
    author: str = ""
    illustrator: str = ""
    year: str = ""
    chapters: str = ""
    rating: float = 0.0
    owned: str = ""
    notes: str = ""

