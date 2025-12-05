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
    id: int
    title: str
    year: str
    seasons: int
    genre: Genre
    rating: float
    rewatch_value: int
    owned: bool
    manga: Manga
    notes: str


@dataclass
class Manga:
    id: int
    title: str
    author: str
    illustrator: str
    year: str
    chapters: int
    genre: Genre
    rating: float
    owned: bool
    anime: Anime
    notes: str


@dataclass
class Genre:
    id: int
    name: str

