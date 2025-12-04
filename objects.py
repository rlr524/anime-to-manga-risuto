from dataclasses import dataclass

@dataclass
class Anime:
    id: int
    title: str
    year: int
    seasons: int
    genre: Genre
    rating: float
    rewatch_value: int
    owned: bool


@dataclass
class Manga:
    id: int
    title: str
    author: str
    illustrator: str
    year: int
    chapters: int
    genre: Genre
    rating: float
    owned: bool


@dataclass
class Genre:
    id: int
    name: str

