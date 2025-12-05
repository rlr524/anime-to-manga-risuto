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