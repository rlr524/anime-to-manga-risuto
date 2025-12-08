"""
Dev 128 Fall 2025 Section 27802
Rob Ranf
Final Project
GitHub Repo: https://github.com/rlr524/anime-to-manga-risuto

ui.py - All logic for the user interface using tkinter
"""

import tkinter as tk
from tkinter import messagebox
import services as svc
from database import Database

class AnimeToMangaUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Anime to Manga Risuto: Your Anime and Manga List")
        self.root.geometry("900x900")

        db = Database.connect()


    def create_menu(self):
        menubar = tk.Menu(self.root)
        self.root.config(menu=menubar)

        crud_menu = tk.Menu(menubar, tearoff=0)
        menubar.add_cascade(label="Choices", menu=crud_menu)

        crud_menu.add_command(label="Add an Anime", command=self.add_anime)
        crud_menu.add_command(label="Add a Manga", command=self.add_manga)
        crud_menu.add_command(label="View an Anime", command=self.view_anime)
        crud_menu.add_command(label="View a Manga", command=self.view_manga)
        crud_menu.add_command(label="Add a Genre", command=self.add_genre)
        crud_menu.add_command(label="View All Genres", command=self.view_genres)
        crud_menu.add_command(label="Delete an Anime", command=self.delete_anime)
        crud_menu.add_command(label="Delete a Manga", command=self.delete_manga)
        crud_menu.add_separator()
        crud_menu.add_command(label="Refresh List", command=self.refresh_list)
        crud_menu.add_separator()
        crud_menu.add_command(label="Exit", command=self.root.quit)


    def add_anime(self):
            # Create popup window
            add_window = tk.Toplevel(self.root)
            add_window.title("Add Anime")
            add_window.geometry("600x600")
            add_window.option_add("*Font", "Arial 14")

            # Form fields - using grid layout for alignment
            tk.Label(add_window, text="Title*:").grid(
                row=0, column=0, sticky='e', padx=5, pady=5)
            first_entry = tk.Entry(add_window, width=30)
            first_entry.grid(row=0, column=1, padx=5, pady=5)
            first_entry.focus()  # Cursor starts here

            tk.Label(add_window, text="Year*:").grid(
                row=1, column=0, sticky='e', padx=5, pady=5)
            last_entry = tk.Entry(add_window, width=30)
            last_entry.grid(row=1, column=1, padx=5, pady=5)

            tk.Label(add_window, text="Seasons*:").grid(
                row=2, column=0, sticky='e', padx=5, pady=5)
            email_entry = tk.Entry(add_window, width=30)
            email_entry.grid(row=2, column=1, padx=5, pady=5)

            tk.Label(add_window, text="Genre:*").grid(
                row=3, column=0, sticky='e', padx=5, pady=5)
            job_title_entry = tk.Entry(add_window, width=30)
            job_title_entry.grid(row=3, column=1, padx=5, pady=5)

            tk.Label(add_window, text="Rating:").grid(
                row=4, column=0, sticky='e', padx=5, pady=5)
            street_address_entry = tk.Entry(add_window, width=30)
            street_address_entry.grid(row=4, column=1, padx=5, pady=5)

            tk.Label(add_window, text="Rewatch Value:").grid(
                row=5, column=0, sticky='e', padx=5, pady=5)
            street_address_2_entry = tk.Entry(add_window, width=30)
            street_address_2_entry.grid(row=5, column=1, padx=5, pady=5)

            tk.Label(add_window, text="Owned:").grid(
                row=6, column=0, sticky='e', padx=5, pady=5)
            city_entry = tk.Entry(add_window, width=30)
            city_entry.grid(row=6, column=1, padx=5, pady=5)

            tk.Label(add_window, text="Manga:").grid(
                row=7, column=0, sticky='e', padx=5, pady=5)
            state_entry = tk.Entry(add_window, width=3)
            state_entry.grid(row=7, column=1, sticky='w', padx=5, pady=5)

            tk.Label(add_window, text="Notes:").grid(
                row=8, column=0, sticky='e', padx=5, pady=5)
            postal_entry = tk.Entry(add_window, width=30)
            postal_entry.grid(row=8, column=1, padx=5, pady=5)


    def add_manga(self):
            # Create popup window
            add_window = tk.Toplevel(self.root)
            add_window.title("Add Manga")
            add_window.geometry("600x600")
            add_window.option_add("*Font", "Arial 14")

            # Form fields - using grid layout for alignment
            tk.Label(add_window, text="Title*:").grid(
                row=0, column=0, sticky='e', padx=5, pady=5)
            first_entry = tk.Entry(add_window, width=30)
            first_entry.grid(row=0, column=1, padx=5, pady=5)
            first_entry.focus()  # Cursor starts here

            tk.Label(add_window, text="Year*:").grid(
                row=1, column=0, sticky='e', padx=5, pady=5)
            last_entry = tk.Entry(add_window, width=30)
            last_entry.grid(row=1, column=1, padx=5, pady=5)

            tk.Label(add_window, text="Chapters*:").grid(
                row=2, column=0, sticky='e', padx=5, pady=5)
            email_entry = tk.Entry(add_window, width=30)
            email_entry.grid(row=2, column=1, padx=5, pady=5)

            tk.Label(add_window, text="Genre:*").grid(
                row=3, column=0, sticky='e', padx=5, pady=5)
            job_title_entry = tk.Entry(add_window, width=30)
            job_title_entry.grid(row=3, column=1, padx=5, pady=5)

            tk.Label(add_window, text="Rating:").grid(
                row=4, column=0, sticky='e', padx=5, pady=5)
            street_address_entry = tk.Entry(add_window, width=30)
            street_address_entry.grid(row=4, column=1, padx=5, pady=5)

            tk.Label(add_window, text="Author:").grid(
                row=5, column=0, sticky='e', padx=5, pady=5)
            street_address_2_entry = tk.Entry(add_window, width=30)
            street_address_2_entry.grid(row=5, column=1, padx=5, pady=5)

            tk.Label(add_window, text="Illustrator:").grid(
                row=6, column=0, sticky='e', padx=5, pady=5)
            street_address_2_entry = tk.Entry(add_window, width=30)
            street_address_2_entry.grid(row=6, column=1, padx=5, pady=5)

            tk.Label(add_window, text="Owned:").grid(
                row=7, column=0, sticky='e', padx=5, pady=5)
            city_entry = tk.Entry(add_window, width=30)
            city_entry.grid(row=7, column=1, padx=5, pady=5)

            tk.Label(add_window, text="Anime:").grid(
                row=8, column=0, sticky='e', padx=5, pady=5)
            state_entry = tk.Entry(add_window, width=3)
            state_entry.grid(row=8, column=1, sticky='w', padx=5, pady=5)

            tk.Label(add_window, text="Notes:").grid(
                row=9, column=0, sticky='e', padx=5, pady=5)
            postal_entry = tk.Entry(add_window, width=30)
            postal_entry.grid(row=9, column=1, padx=5, pady=5)


