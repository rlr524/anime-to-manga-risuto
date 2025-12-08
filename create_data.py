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
               VALUES ('Attack On Titan', '2013-2023', 4, 9.9, "Yes", 'Attack on Titan has received universal 
               critical acclaim since its debut in 2013 and is widely regarded as one of the greatest anime series, 
               and television series of any genre, of all time. Critics and audiences have praised the show for its 
               storytelling, animation, action sequences, characters, voice acting (original and dubbed), soundtrack, 
               and dark themes. The series received numerous accolades, achieved widespread popularity globally, and 
               is regarded as having heavily contributed to the expansion of anime''s international audience and 
               movement into the popular mainstream.')''')
cursor.execute('''INSERT INTO animes(title, year, seasons, rating, owned, notes)
               VALUES ('Steins;Gate', '2011-2018', 2, 9.7, "No", 'Steins;Gate received critical acclaim, 
               praised for its character development and themes of time travel, human nature and its perspective on 
               post-traumatic stress disorder (PTSD). It is considered to be one of the best anime series of all time 
               by critics and fans alike. The series has spawned four original net animation (ONA) episodes and a 
               follow-up film. A sequel anime adaptation titled Steins;Gate 0, based on the 2015 visual novel of the 
               same name, premiered in 2018.')''')
cursor.execute('''INSERT INTO animes(title, year, seasons, rating, owned, notes)
               VALUES ('The Melancholy of Haruhui Suzumiya', '2009', 1, 9.3, "Yes", 'Kyon is a sardonic, 
               witty student at North High School in Nishinomiya who once sought to have an extraordinary life, but 
               after deeming the notion childish, now seeks little more than a normal life. At school, however, he ends 
               up befriending Haruhi Suzumiya, an eccentric schoolgirl that sits behind him in class who is constantly 
               seeking to make life more interesting for herself, ranging from doing her hair a certain way each day 
               of the week to actively searching for supernatural phenomena and figures. One day, Kyon accidentally 
               plants in Haruhi''s head the idea for her to start a club to engage in her eccentricities, so she 
               establishes a club called the "SOS Brigade" short for "Spreading excitement all Over the world with 
               Haruhi Suzumiya Brigade"')''')
cursor.execute('''INSERT INTO animes(title, year, seasons, rating, owned, notes)
               VALUES ('Naruto', '2002-2007', 2, 8.2, "No", 'A powerful fox known as the Nine-Tails attacks 
               Konoha, the hidden leaf village in the Land of Fire, one of the Five Great Shinobi Countries in the 
               Ninja World. In response, the leader of Konoha and the Fourth Hokage, Minato Namikaze, at the cost of 
               his life, seals the fox inside the body of his newborn son, Naruto Uzumaki, making him a host of the 
               beast. The Third Hokage returns from retirement to become the leader of Konoha again. Naruto is 
               often scorned by Konoha''s villagers for being the host of the Nine-Tails. Due to a decree by the 
               Third Hokage forbidding any mention of these events, Naruto learns nothing about the Nine-Tails 
               until 12 years later, when Mizuki, a renegade ninja, reveals the truth to him.')''')


# create some records of data for manga
cursor.execute('''INSERT INTO mangas(title, author, illustrator, year, chapters, rating, owned, notes)
               VALUES ('Death Note', 'Tsugumi Ōba', 'Takeshi Obata', '2003-2006', 108, 9.5, "No", 'Death Note 
               follows Light Yagami, a genius high school student who discovers a mysterious notebook, the Death 
               Note, which belonged to the shinigami Ryuk and kills anyone whose name is written in its pages. The 
               series centers on Light''s use of the Death Note to carry out a worldwide massacre of individuals he 
               deems immoral to create a crime-free society, using the alias of a god-like vigilante named Kira, and 
               the efforts of an elite Japanese police task force, led by the detective L, to apprehend him.')''')
cursor.execute('''INSERT INTO mangas(title, author, illustrator, year, chapters, rating, owned, notes)
               VALUES ('Attack on Titan', 'Hajime Isamaya', 'Hajime Isayama', '2009-2021', 139, 9.8, "Yes", 'Attack 
               on Titan is set in a world where humanity lives inside cities surrounded by enormous walls due to the 
               Titans, gigantic humanoid creatures who devour humans seemingly without reason. The story centers 
               around Eren Yeager, alongside his childhood friends, Mikasa Ackerman and Armin Arlert, whose lives are 
               changed forever after the appearance of a Colossus Titan brings about the destruction of their home 
               town and the death of Eren''s mother. Vowing revenge and to reclaim the world from the Titans, Eren, 
               Mikasa and Armin join the Survey Corps, an elite group of soldiers who fight Titans outside the 
               walls.')''')
cursor.execute('''INSERT INTO mangas(title, author, illustrator, year, chapters, rating, owned, notes)
               VALUES ('Jojo''s Bizarre Adventure', 'Hirohiko Araki', 'Hirohiko Araki', '1987-Present', 138, 8.8, 
                       "No", 'JoJo''s Bizarre Adventure is well known for its art style and poses, frequent 
                       references to Western popular music and fashion, and battles centered around Stands, 
                       psycho-spiritual manifestations of the person''s fighting spirit with unique supernatural 
                       abilities. The series had over 120 million copies in circulation by August 2023, making it 
                       one of the best-selling manga series in history, and it has spawned a media franchise 
                       including one-shot manga, light novels, and video games.')''')


# commit the changes to the database
conn.commit()

# close the database
conn.close()