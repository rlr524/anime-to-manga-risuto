"""
Dev 128 Fall 2025 Section 27802
Rob Ranf
Final Project
GitHub Repo: https://github.com/rlr524/anime-to-manga-risuto

services.py - All functions that interact with the database performing CRUD operations.
"""

import logging
from database import Database
from models import Anime, Manga, Genre
from contextlib import closing
from typing import Any, List, Optional

db = Database()
conn = db.connect()

def make_genre(row: Any) -> Genre:
    """
    Creates a new Genre instance given input from a SQL query
    :param row: A parameter of type Any that is passed to the initializer of a Genre instance
    :return: An instance of the Genre class
    """
    return Genre(row["genre_id"], row["name"])


def make_anime(row: Any) -> Anime:
    """
    Creates a new Anime instance given input from a SQL query
    :param row: A parameter of type Any that is passed to the initializer of an Anime instance
    :return: An instance of the Anime class
    """
    return Anime(row["anime_id"], row["title"], row["year"], row["seasons"], make_genre(row), row["rating"],
                 row["rewatch_value"], row["owned"], row["manga_id"], row["notes"])


def make_manga(row: Any) -> Manga:
    """
    Creates a new Manga instance given input from a SQL query
    :param row: A parameter of type Any that is passed to the initializer of a Manga instance
    :return: An instance of the Manga class
    """
    return Manga(row["manga_id"], row["title"], row["author"], row["illustrator"], row["year"], row["chapters"],
                 make_genre(row), row["rating"], row["owned"], row["anime_id"], row["notes"])


def make_anime_list(anime_results: Any) -> List[Anime]:
    """
    Creates a List of Anime instances given input from a SQL query
    :param anime_results: A parameter of type Any that represents a List of anime rows from a DB query
    :return: A List of instances of the Anime class
    """
    anime: List[Anime] = []
    for r in anime_results:
        anime.append(make_anime(r))
    return anime


def make_manga_list(manga_results: Any) -> List[Manga]:
    """
    Creates a List of Manga instances given input from a SQL query
    :param manga_results: A parameter of type Any that represents a List of manga rows from a DB query
    :return: A List of instances of the Manga class
    """
    mangas: List[Manga] = []
    for r in manga_results:
        mangas.append(make_manga(r))
    return mangas


def get_anime(anime_id: int) -> Optional[Anime]:
    """
    Get a single anime given an anime's id
    :param anime_id: An int representing the id of an anime
    :return: An Optional of an Anime object or None of the anime_id doesn't exist
    """
    q = '''SELECT a.anime_id, a.title, a.year, a.seasons, a.genre_id, a.rating, a.rewatch_value, a.owned, 
                  a.manga_id, a.notes
           FROM animes a join genres g ON g.genre_id = a.genre_id
           WHERE a.anime_id = ?'''
    with closing(conn.cursor()) as c:
        c.execute(q, (anime_id,))
        anime_row: Any = c.fetchone()
        if anime_row:
            return make_anime(anime_row)
        else:
            return None


def get_manga(manga_id: int) -> Optional[Manga]:
    """
    Get a single manga given a manga's id
    :param manga_id: An int representing the id of a manga
    :return: An Optional of a Manga object or None of the manga_id doesn't exist
    """
    q = '''SELECT m.manga_id, m.title, m.author, m.illustrator, m.year, m.chapters, m.genre_id, m.rating, m.owned,
                  m.anime_id, m.notes
           FROM mangas m join genres g ON g.genre_id = m.genre_id
           WHERE m.manga_id = ?'''
    with closing(conn.cursor()) as c:
        c.execute(q, (manga_id,))
        manga_row: Any = c.fetchone()
        if manga_row:
            return make_manga(manga_row)
        else:
            return None


def get_all_anime() -> List[Anime]:
    """
    Get all anime in the database
    :return: A List of Anime objects representing all Anime
    """
    q = '''SELECT a.anime_id, a.title, a.year, a.seasons, a.genre_id, a.rating, a.owned 
           FROM animes a JOIN genres g ON g.genre_id = a.genre_id'''

    with closing(conn.cursor()) as c:
        c.execute(q)
        results = c.fetchall()

    animes: List[Anime] = []
    for r in results:
        animes.append(make_anime(r))
    return animes


def get_all_manga() -> List[Manga]:
    """
    Get all manga in the database
    :return: A List of Manga objects representing all manga titles
    """
    q = '''SELECT m.manga_id, m.title, m.author, m.illustrator, m.year, m.chapters, m.genre_id, m.rating
           FROM mangas m JOIN genres g ON g.genre_id = m.genre_id'''

    with closing(conn.cursor()) as c:
        c.execute(q)
        results = c.fetchall()

    mangas: List[Manga] = []
    for r in results:
        mangas.append(make_manga(r))
    return mangas


def get_all_genres() -> List[Genre]:
    """
    Get all genres in the database
    :return: A list of Genre objects
    """
    q = '''SELECT genre_id, name FROM genres '''
    with closing(conn.cursor()) as c:
        c.execute(q)
        results = c.fetchall()

    genres: List[Genre] = []
    for r in results:
        genres.append(make_genre(r))
    return genres


def get_genre(genre_id: int) -> Optional[Genre]:
    """
    Get a genre given a specific genre id
    :param genre_id: An int value representing the genre_id of a Genre object
    :return: An optional of a Genre object, or None if the genre_id does not exist
    """
    q = '''SELECT genre_id, name FROM genres WHERE genre_id = ?'''
    with closing(conn.cursor()) as c:
        c.execute(q, (genre_id,))
        genre_row: Any = c.fetchone()
        if genre_row:
            return make_genre(genre_row)
        else:
            return None


def add_anime (anime: Anime) -> None:
    """
    Add a single anime to the database. Includes validation of required fields that do not have a default value as
    well as error handling for database transaction commit errors. This error handling is necessary on any function
    that performs a transaction commit on the database in order to comply with ACID assurance.
    :param anime: An Anime object to insert
    :return: None
    :raises: A SQLite Database error if insertion fails.
    """
    # account for that the genre id is passed as an int however is evaluated as a Genre object with an id or genre_id
    if getattr(anime, "genre", None) is None:
        raise ValueError("anime genre is required")

    genre_value = anime.genre
    if isinstance(genre_value, int):
        genre_id = genre_value
    else:
        genre_id = getattr(genre_value, "id", None) or getattr(genre_value, "genre_id", None)

    if genre_id is None:
        raise ValueError("drama genre is required")

    if not getattr(anime, "title", None):
        raise ValueError("anime title is required")
    if not getattr(anime, "year", None):
        raise ValueError("anime year is required")
    if not getattr(anime, "seasons", None):
        raise ValueError("anime seasons is required")

    s = '''INSERT INTO animes (title, year, seasons, genre_id, rating, rewatch_value, owned, manga_id, notes) 
           VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)'''
    try:
        with closing(conn.cursor()) as c:
            c.execute(s, (anime.title, anime.year, anime.seasons, anime.genre, anime.rating, anime.rewatch_value,
                          anime.owned, anime.manga, anime.notes))
        conn.commit()
    except conn.DatabaseError as e:
        try:
            conn.rollback()
        except conn.OperationalError:
            logging.exception("Failed to roll back transaction after insert failure")
        logging.exception(f"Failed to insert anime {e}")
        raise


def add_manga (manga: Manga) -> None:
    """
    Add a single manga to the database. Includes validation of required fields that do not have a default value as
    well as error handling for database transaction commit errors. This error handling is necessary on any function
    that performs a transaction commit on the database in order to comply with ACID assurance.
    :param manga: A Manga object to insert
    :return: None
    :raises: A SQLite Database error if insertion fails.
    """
    # account for that the genre id is passed as an int however is evaluated as a Genre object with an id or genre_id
    if getattr(manga, "genre", None) is None:
        raise ValueError("manga genre is required")

    genre_value = manga.genre
    if isinstance(genre_value, int):
        genre_id = genre_value
    else:
        genre_id = getattr(genre_value, "id", None) or getattr(genre_value, "genre_id", None)

    if genre_id is None:
        raise ValueError("manga genre is required")

    if not getattr(manga, "title", None):
        raise ValueError("anime title is required")
    if not getattr(manga, "year", None):
        raise ValueError("anime year is required")
    if not getattr(manga, "chapters", None):
        raise ValueError("manga chapters is required")

    s = '''INSERT INTO mangas (title, author, illustrator, year, chapters, genre_id, rating, owned, anime_id, notes) 
           VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)'''
    try:
        with closing(conn.cursor()) as c:
            c.execute(s, (manga.title, manga.author, manga.illustrator, manga.year, manga.chapters, manga.genre,
                          manga.rating, manga.owned, manga.anime, manga.notes))
        conn.commit()
    except conn.DatabaseError as e:
        try:
            conn.rollback()
        except conn.OperationalError:
            logging.exception("Failed to roll back transaction after insert failure")
        logging.exception(f"Failed to insert manga {e}")
        raise


def delete_anime(anime_id: int) -> None:
    """
    Deletes a specific anime from the database performing a hard delete
    :param anime_id: anime_id of the specific anime
    :return: None
    :raises: A Database error if delete fails
    """
    s = '''DELETE FROM main.animes WHERE anime_id = ?'''
    try:
        with closing(conn.cursor()) as c:
            c.execute(s, (anime_id,))
        conn.commit()
    except conn.DatabaseError as e:
        try:
            conn.rollback()
        except conn.OperationalError:
            logging.exception("Failed to roll back transaction after delete failure")
        logging.exception(f"Failed to delete anime {e}")
        raise


def delete_manga(manga_id: int) -> None:
    """
    Deletes a specific manga from the database performing a hard delete
    :param manga_id: manga_id of the specific manga
    :return: None
    :raises: A Database error if delete fails
    """
    s = '''DELETE FROM main.mangas WHERE mangas.manga_id = ?'''
    try:
        with closing(conn.cursor()) as c:
            c.execute(s, (manga_id,))
        conn.commit()
    except conn.DatabaseError as e:
        try:
            conn.rollback()
        except conn.OperationalError:
            logging.exception("Failed to roll back transaction after delete failure")
        logging.exception(f"Failed to delete manga {e}")
        raise
