"""
Dev 128 Fall 2025 Section 27802
Rob Ranf
Final Project
GitHub Repo: https://github.com/rlr524/anime-to-manga-risuto

services.py - All functions that interact with the database performing CRUD operations.
"""

import logging
from database import Database
from models import Anime, Manga
from contextlib import closing
from typing import Any, List, Optional

db = Database()
conn = db.connect()

def get_anime(anime_id: int) -> Optional[Anime]:
    """
    Get a single anime given an anime's id
    :param anime_id: An int representing the id of an anime
    :return: An Optional of an Anime object or None of the anime_id doesn't exist
    """
    q = '''SELECT a.anime_id, a.title, a.year, a.seasons, a.rating, a.owned, a.notes
           FROM animes a
           WHERE a.anime_id = ?'''
    with closing(conn.cursor()) as c:
        c.execute(q, (anime_id,))
        anime: Any = c.fetchone()
        if anime:
            return anime
        else:
            return None


def get_manga(manga_id: int) -> Optional[Manga]:
    """
    Get a single manga given a manga's id
    :param manga_id: An int representing the id of a manga
    :return: An Optional of a Manga object or None of the manga_id doesn't exist
    """
    q = '''SELECT m.manga_id, m.title, m.author, m.illustrator, m.year, m.chapters, m.rating, m.owned, m.notes
           FROM mangas m
           WHERE m.manga_id = ?'''
    with closing(conn.cursor()) as c:
        c.execute(q, (manga_id,))
        manga: Any = c.fetchone()
        if manga:
            return manga
        else:
            return None


def get_all_anime() -> List[Anime]:
    """
    Get all anime in the database
    :return: A List of Anime objects representing all Anime
    """
    q = '''SELECT a.anime_id, a.title, a.year, a.seasons, a.rating, a.owned 
           FROM animes a'''

    with closing(conn.cursor()) as c:
        c.execute(q)
        animes = c.fetchall()

    return animes


def get_all_manga() -> List[Manga]:
    """
    Get all manga in the database
    :return: A List of Manga objects representing all manga titles
    """
    q = '''SELECT m.manga_id, m.title, m.author, m.illustrator, m.year, m.chapters, m.rating, m.owned
           FROM mangas m'''

    with closing(conn.cursor()) as c:
        c.execute(q)
        mangas = c.fetchall()

    return mangas


def add_anime (anime: Anime) -> None:
    """
    Add a single anime to the database. Includes validation of required fields that do not have a default value as
    well as error handling for database transaction commit errors. This error handling is necessary on any function
    that performs a transaction commit on the database in order to comply with ACID assurance.
    :param anime: An Anime object to insert
    :return: None
    :raises: A SQLite Database error if insertion fails.
    """
    if not getattr(anime, "title", None):
        raise ValueError("anime title is required")
    if not getattr(anime, "year", None):
        raise ValueError("anime year is required")
    if not getattr(anime, "seasons", None):
        raise ValueError("anime seasons is required")

    s = '''INSERT INTO animes (title, year, seasons, rating, owned, notes) 
           VALUES (?, ?, ?, ?, ?, ?)'''
    try:
        with closing(conn.cursor()) as c:
            c.execute(s, (anime.title, anime.year, anime.seasons, anime.rating, anime.owned, anime.notes))
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
    if not getattr(manga, "title", None):
        raise ValueError("anime title is required")
    if not getattr(manga, "year", None):
        raise ValueError("anime year is required")
    if not getattr(manga, "chapters", None):
        raise ValueError("manga chapters is required")

    s = '''INSERT INTO mangas (title, author, illustrator, year, chapters, rating, owned, notes) 
           VALUES (?, ?, ?, ?, ?, ?, ?, ?)'''
    try:
        with closing(conn.cursor()) as c:
            c.execute(s, (manga.title, manga.author, manga.illustrator, manga.year, manga.chapters,
                          manga.rating, manga.owned, manga.notes))
        conn.commit()
    except conn.DatabaseError as e:
        try:
            conn.rollback()
        except conn.OperationalError:
            logging.exception("Failed to roll back transaction after insert failure")
        logging.exception(f"Failed to insert manga {e}")
        raise


def delete_anime(anime_id: int) -> Any:
    """
    Deletes a specific anime from the database performing a hard delete
    :param anime_id: anime_id of the specific anime
    :return: The number of rows affected or an exception
    :raises: A Database error if delete fails
    """
    s = '''DELETE FROM main.animes WHERE anime_id = ?'''
    try:
        with closing(conn.cursor()) as c:
            c.execute(s, (anime_id,))
            rows_affected = c.rowcount
        conn.commit()
        return rows_affected > 0
    except conn.DatabaseError as e:
        try:
            conn.rollback()
        except conn.OperationalError:
            logging.exception("Failed to roll back transaction after delete failure")
        logging.exception(f"Failed to delete anime {e}")
        raise


def delete_manga(manga_id: int) -> Any:
    """
    Deletes a specific manga from the database performing a hard delete
    :param manga_id: manga_id of the specific manga
    :return: The number of rows effected or an exception
    :raises: A Database error if delete fails
    """
    s = '''DELETE FROM main.mangas WHERE mangas.manga_id = ?'''
    try:
        with closing(conn.cursor()) as c:
            c.execute(s, (manga_id,))
            rows_affected = c.rowcount
        conn.commit()
        return rows_affected > 0
    except conn.DatabaseError as e:
        try:
            conn.rollback()
        except conn.OperationalError:
            logging.exception("Failed to roll back transaction after delete failure")
        logging.exception(f"Failed to delete manga {e}")
        raise


def validate_anime_data(title, year, seasons):
    if not title or not title.strip():
        return False, "Title is required"

    if not year or not year.strip():
        return False, "Year is required"

    if not seasons or not seasons.strip():
        return False, "Number of seasons is required"

    # All validation passed
    return True, ""


def validate_manga_data(title, year, chapters):
    if not title or not title.strip():
        return False, "Title is required"

    if not year or not year.strip():
        return False, "Year is required"

    if not chapters or not chapters.strip():
        return False, "Number of chapters is required"

    # All validation passed
    return True, ""