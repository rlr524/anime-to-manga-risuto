"""
Dev 128 Fall 2025 Section 27802
Rob Ranf
Final Project
GitHub Repo: https://github.com/rlr524/anime-to-manga-risuto

create_data.py - A utility file used to create database tables and starter data.
"""

# import the sqlite3 database module
import sqlite3

# create the database file and a connection
conn = sqlite3.connect("anime.db")

# create a cursor
cursor = conn.cursor()

# create the tables if they don't already exist
cursor.execute('''CREATE TABLE IF NOT EXISTS animes (anime_id INTEGER PRIMARY KEY, title TEXT, year TEXT, 
                                                     seasons TEXT, rating FLOAT, owned TEXT, notes TEXT)''')
cursor.execute('''CREATE TABLE IF NOT EXISTS mangas (manga_id INTEGER PRIMARY KEY, title TEXT, author TEXT, 
                                                     illustrator TEXT, year TEXT, chapters TEXT, 
                                                     rating FLOAT, owned TEXT, notes TEXT)''')


# create some records of data for anime
cursor.execute('''INSERT INTO animes(title, year, seasons, rating, owned, notes)
               VALUES ('Attack On Titan', '2013-2023', 4, 9.9, "Yes", 'Attack on Titan has received universal acclaim as one of the best anime of all time.')''')
cursor.execute('''INSERT INTO animes(title, year, seasons, rating, owned, notes)
               VALUES ('Steins;Gate', '2011-2018', 2, 9.7, "No", 'Steins;Gate received critical acclaim, praised for its character development and themes of time travel, human nature and its perspective on post-traumatic stress disorder (PTSD).')''')
cursor.execute('''INSERT INTO animes(title, year, seasons, rating, owned, notes)
               VALUES ('The Melancholy of Haruhui Suzumiya', '2009', 1, 9.3, "Yes", '')''')
cursor.execute('''INSERT INTO animes(title, year, seasons, rating, owned, notes)
               VALUES ('Naruto', '2002-2007', 2, 8.2, "No", '')''')


# create some records of data for manga
cursor.execute('''INSERT INTO mangas(title, author, illustrator, year, chapters, rating, owned, notes)
               VALUES ('Death Note', 'Tsugumi Ōba', 'Takeshi Obata', '2003-2006', 108, 9.5, "No", '')''')
cursor.execute('''INSERT INTO mangas(title, author, illustrator, year, chapters, rating, owned, notes)
               VALUES ('Attack on Titan', 'Hajime Isamaya', 'Hajime Isayama', '2009-2021', 139, 9.8, "Yes", '')''')
cursor.execute('''INSERT INTO mangas(title, author, illustrator, year, chapters, rating, owned, notes)
               VALUES ('Jojo''s Bizarre Adventure', 'Hirohiko Araki', 'Hirohiko Araki', '1987-Present', 138, 8.8, 
                       "No", '')''')


# commit the changes to the database
conn.commit()

# close the database
conn.close()