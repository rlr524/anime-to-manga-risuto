"""
Dev 128 Fall 2025 Section 27802
Rob Ranf
Final Project
GitHub Repo: https://github.com/rlr524/anime-to-manga-risuto

database.py - A convenience module used to abstract database connection details from the business logic and ui.
"""

import sqlite3

class Database:
    @staticmethod
    def connect() -> sqlite3.Connection:
        """
        A reusable connect method. The creation of a Database class allows for the database to be easily updated
        to a different database engine without needing to touch the model, services layer, or user interface. This
        is generally equivalent to using the Repository pattern in Java and other languages to abstract away the
        database access layer.
        :return: A SQLite3 Connection object
        """
        conn: sqlite3.Connection = sqlite3.connect("anime.db")
        conn.row_factory = sqlite3.Row

        return conn

    def close(self):
        """
        A reusable close method that can be called to close the database connection in instances in which the
        closing context from the contextlib library isn't used.
        :return: None
        """
        conn: sqlite3.Connection = self.connect()
        if conn:
            conn.close()