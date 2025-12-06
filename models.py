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
    seasons: int = 0
    genre: Genre = None
    rating: float = 0.0
    rewatch_value: int = 0
    owned: bool = False
    manga: Manga = None
    notes: str = ""


@dataclass
class Manga:
    id: int = 0
    title: str = ""
    author: str = ""
    illustrator: str = ""
    year: str = ""
    chapters: int = 0
    genre: Genre = None
    rating: float = 0.0
    owned: bool = False
    anime: Anime = None
    notes: str = ""


@dataclass
class Genre:
    id: int = 0
    name: str = ""

