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
from models import Anime, Manga

class AnimeToMangaUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Anime to Manga Risuto: Your Anime and Manga List")
        self.root.geometry("1400x1000")

        self.create_menu()
        self.create_layout()

        self.refresh_list()


    def create_menu(self):
        menubar = tk.Menu(self.root)
        self.root.config(menu=menubar)

        crud_menu = tk.Menu(menubar, tearoff=0)
        menubar.add_cascade(label="Choices", menu=crud_menu)

        crud_menu.add_command(label="Add an Anime", command=self.add_anime)
        crud_menu.add_command(label="Add a Manga", command=self.add_manga)
        crud_menu.add_command(label="View an Anime", command=self.view_anime)
        crud_menu.add_command(label="View a Manga", command=self.view_manga)
        crud_menu.add_command(label="Delete an Anime", command=self.delete_anime)
        crud_menu.add_command(label="Delete a Manga", command=self.delete_manga)
        crud_menu.add_separator()
        crud_menu.add_command(label="Refresh List", command=self.refresh_list)
        crud_menu.add_separator()
        crud_menu.add_command(label="Exit", command=self.root.quit)

    def create_layout(self):
        main_frame = tk.Frame(self.root)
        main_frame.pack(fill="both", expand=True, padx=10, pady=10)

        tk.Label(main_frame, text="Anime and Manga List", font=('Arial', 14, 'bold')).pack(pady=5)

        listbox_frame = tk.Frame(main_frame)
        listbox_frame.pack(fill="both", expand=True)

        scrollbar = tk.Scrollbar(listbox_frame)
        scrollbar.pack(side="right", fill="y")

        self.listbox = tk.Listbox(listbox_frame,
                                  yscrollcommand=scrollbar.set,
                                  font=('Arial', 14))
        self.listbox.pack(side="left", fill="both", expand=True)

        scrollbar.config(command=self.listbox.yview)

        button_frame = tk.Frame(main_frame)
        button_frame.pack(pady=10)

        tk.Button(button_frame, text="Add Anime",
                 command=self.add_anime, width=10).grid(row=0, column=0, padx=5)
        tk.Button(button_frame, text="Add Manga",
                 command=self.add_manga, width=10).grid(row=1, column=0, padx=5)
        tk.Button(button_frame, text="View Anime",
                 command=self.view_anime, width=10).grid(row=0, column=1, padx=5)
        tk.Button(button_frame, text="View Manga ",
                 command=self.view_manga, width=10).grid(row=1, column=1, padx=5)
        tk.Button(button_frame, text="Delete Anime",
                 command=self.delete_anime, width=10).grid(row=0, column=2, padx=5)
        tk.Button(button_frame, text="Delete Manga ",
                 command=self.delete_manga, width=10).grid(row=1, column=2, padx=5)


    def add_anime(self):
            # Create popup window
            add_window = tk.Toplevel(self.root)
            add_window.title("Add Anime")
            add_window.geometry("600x600")
            add_window.option_add("*Font", "Arial 14")

            # Form fields - using grid layout for alignment
            tk.Label(add_window, text="Title*:").grid(
                row=0, column=0, sticky='e', padx=5, pady=5)
            title_entry = tk.Entry(add_window, width=30)
            title_entry.grid(row=0, column=1, padx=5, pady=5)
            title_entry.focus()  # Cursor starts here

            tk.Label(add_window, text="Year*:").grid(
                row=1, column=0, sticky='e', padx=5, pady=5)
            year_entry = tk.Entry(add_window, width=30)
            year_entry.grid(row=1, column=1, padx=5, pady=5)

            tk.Label(add_window, text="Seasons*:").grid(
                row=2, column=0, sticky='e', padx=5, pady=5)
            season_entry = tk.Entry(add_window, width=30)
            season_entry.grid(row=2, column=1, padx=5, pady=5)

            tk.Label(add_window, text="Rating:").grid(
                row=3, column=0, sticky='e', padx=5, pady=5)
            rating_entry = tk.Entry(add_window, width=30)
            rating_entry.grid(row=3, column=1, padx=5, pady=5)

            tk.Label(add_window, text="Owned?:").grid(
                row=4, column=0, sticky='e', padx=5, pady=5)
            owned_entry = tk.Entry(add_window, width=30)
            owned_entry.grid(row=4, column=1, padx=5, pady=5)

            tk.Label(add_window, text="Notes:").grid(
                row=5, column=0, sticky='ne', padx=5, pady=5)
            notes_text = tk.Text(add_window, height=10, width=30)
            notes_text.grid(row=5, column=1, padx=5, pady=5)

            def save_anime():
                title = title_entry.get().strip()
                year = year_entry.get().strip()
                season = season_entry.get().strip()
                rating = float(rating_entry.get().strip())
                owned = owned_entry.get().strip()
                notes = notes_text.get("1.0", tk.END).strip()

                # Validate using business logic layer
                is_valid, error_message = svc.validate_anime_data(title, year, season)

                if not is_valid:
                    messagebox.showerror("Validation Error", error_message)
                    return

                # Call business logic to add anime
                new_anime = Anime(id, title, year, season, rating, owned, notes)
                svc.add_anime(new_anime)

                # Show success message
                messagebox.showinfo("Success",f"Anime added successfully!\nTitle: {title}")

                # Close the popup window
                add_window.destroy()

                # Refresh the main list to show the new person
                self.refresh_list()

            def cancel_window():
                add_window.destroy()

            # Save button
            tk.Button(add_window, text="Save", command=save_anime, width=10).grid(row=10, column=0, pady=10)

            # Cancel button
            tk.Button(add_window, text="Cancel", command=cancel_window, width=10).grid(row=10, column=1, pady=10)


    def add_manga(self):
            # Create popup window
            add_window = tk.Toplevel(self.root)
            add_window.title("Add Manga")
            add_window.geometry("600x600")
            add_window.option_add("*Font", "Arial 14")

            # Form fields - using grid layout for alignment
            tk.Label(add_window, text="Title*:").grid(
                row=0, column=0, sticky='e', padx=5, pady=5)
            title_entry = tk.Entry(add_window, width=30)
            title_entry.grid(row=0, column=1, padx=5, pady=5)
            title_entry.focus()  # Cursor starts here

            tk.Label(add_window, text="Year*:").grid(
                row=1, column=0, sticky='e', padx=5, pady=5)
            year_entry = tk.Entry(add_window, width=30)
            year_entry.grid(row=1, column=1, padx=5, pady=5)

            tk.Label(add_window, text="Chapters*:").grid(
                row=2, column=0, sticky='e', padx=5, pady=5)
            chapter_entry = tk.Entry(add_window, width=30)
            chapter_entry.grid(row=2, column=1, padx=5, pady=5)

            tk.Label(add_window, text="Rating:").grid(
                row=3, column=0, sticky='e', padx=5, pady=5)
            rating_entry = tk.Entry(add_window, width=30)
            rating_entry.grid(row=3, column=1, padx=5, pady=5)

            tk.Label(add_window, text="Author:").grid(
                row=4, column=0, sticky='e', padx=5, pady=5)
            author_entry = tk.Entry(add_window, width=30)
            author_entry.grid(row=4, column=1, padx=5, pady=5)

            tk.Label(add_window, text="Illustrator:").grid(
                row=5, column=0, sticky='e', padx=5, pady=5)
            illustrator_entry = tk.Entry(add_window, width=30)
            illustrator_entry.grid(row=5, column=1, padx=5, pady=5)

            tk.Label(add_window, text="Owned:").grid(
                row=6, column=0, sticky='e', padx=5, pady=5)
            owned_entry = tk.Entry(add_window, width=30)
            owned_entry.grid(row=6, column=1, padx=5, pady=5)

            tk.Label(add_window, text="Notes:").grid(
                row=7, column=0, sticky='ne', padx=5, pady=5)
            notes_text = tk.Text(add_window, height=10, width=30)
            notes_text.grid(row=7, column=1, padx=5, pady=5)

            def save_manga():
                title = title_entry.get().strip()
                year = year_entry.get().strip()
                chapter = chapter_entry.get().strip()
                rating = float(rating_entry.get().strip())
                author = author_entry.get().strip()
                illustrator = illustrator_entry.get().strip()
                owned = owned_entry.get().strip()
                notes = notes_text.get("1.0", tk.END).strip()

                # Validate using business logic layer
                is_valid, error_message = svc.validate_anime_data(title, year, chapter)

                if not is_valid:
                    messagebox.showerror("Validation Error", error_message)
                    return

                # Call business logic to add anime
                new_manga = Manga(id, title, author, illustrator, year, chapter, rating, owned, notes)
                svc.add_manga(new_manga)

                # Show success message
                messagebox.showinfo("Success",f"Manga added successfully!\nTitle: {title}")

                # Close the popup window
                add_window.destroy()

                # Refresh the main list to show the new person
                self.refresh_list()

            def cancel_window():
                add_window.destroy()

            # Save button
            tk.Button(add_window, text="Save", command=save_manga, width=10).grid(row=10, column=0, pady=10)

            # Cancel button
            tk.Button(add_window, text="Cancel", command=cancel_window, width=10).grid(row=10, column=1, pady=10)

    def view_anime(self):
        selection = self.listbox.curselection()
        if not selection:
            messagebox.showwarning("No Selection",
                                   "Please select an anime from the list!")
            return

        anime_info = self.listbox.get(selection[0])

        anime_id = int(anime_info.split(" - ")[0])

        anime = svc.get_anime(anime_id)

        if not anime:
            messagebox.showerror("Error", "Anime not found in database!")
            return

        anime_id, title, year, seasons, rating, owned, notes = anime

        # Create display window
        read_window = tk.Toplevel(self.root)
        read_window.title("Anime Details")
        read_window.geometry("800x600")
        read_window.option_add("*Font", "Arial 14")

        # Format details nicely
        details = f"""
    ID: {anime_id}
    Title: {title}
    Year: {year}
    Seasons: {seasons}
    Rating: {rating}
    Owned?: {owned}
    Notes: {notes}
            """

        # Display as label
        tk.Label(read_window, text=details, wraplength=400,
                 justify='left', font=('Arial', 12)).pack(padx=20, pady=20)

        # Close button
        tk.Button(read_window, text="Close",
                  command=read_window.destroy).pack(pady=10)


    def view_manga(self):
        selection = self.listbox.curselection()
        if not selection:
            messagebox.showwarning("No Selection",
                                   "Please select a manga from the list!")
            return

        manga_info = self.listbox.get(selection[0])

        manga_id = int(manga_info.split(" - ")[0])

        manga = svc.get_manga(manga_id)

        if not manga:
            messagebox.showerror("Error", "Manga not found in database!")
            return

        manga_id, title, author, illustrator, year, chapters, rating, owned, notes = manga

        # Create display window
        read_window = tk.Toplevel(self.root)
        read_window.title("Manga Details")
        read_window.geometry("800x600")
        read_window.option_add("*Font", "Arial 14")

        # Format details nicely
        details = f"""
    ID: {manga_id}
    Title: {title}
    Author: {author}
    Illustrator: {illustrator}
    Year: {year}
    Chapters: {chapters}
    Rating: {rating}
    Owned?: {owned}
    Notes: {notes}
            """

        # Display as label
        tk.Label(read_window, text=details, wraplength=400,
                 justify='left', font=('Arial', 12)).pack(padx=20, pady=20)

        # Close button
        tk.Button(read_window, text="Close",
                  command=read_window.destroy).pack(pady=10)


    def delete_anime(self):
        selection = self.listbox.curselection()
        if not selection:
            messagebox.showwarning("No Selection",
                                   "Please select an anime to delete!")
            return

        anime_info = self.listbox.get(selection[0])
        anime_id = int(anime_info.split(" - ")[0])

        confirm = messagebox.askyesno(
            "Confirm Delete",
            f"Are you sure you want to delete:\n\n{anime_info}\n\nThis cannot be undone!"
        )

        if not confirm:
            return

        success = svc.delete_anime(anime_id)

        if success:
            messagebox.showinfo("Success", "Anime deleted successfully!")
            self.refresh_list()
        else:
            messagebox.showerror("Error", "Failed to delete anime!")


    def delete_manga(self):
        selection = self.listbox.curselection()
        if not selection:
            messagebox.showwarning("No Selection",
                                   "Please select a manga to delete!")
            return

        manga_info = self.listbox.get(selection[0])
        manga_id = int(manga_info.split(" - ")[0])

        confirm = messagebox.askyesno(
            "Confirm Delete",
            f"Are you sure you want to delete:\n\n{manga_info}\n\nThis cannot be undone!"
        )

        if not confirm:
            return

        success = svc.delete_manga(manga_id)

        if success:
            messagebox.showinfo("Success", "Manga deleted successfully!")
            self.refresh_list()
        else:
            messagebox.showerror("Error", "Failed to delete manga!")




    def refresh_list(self):
        self.listbox.delete(0, tk.END)

        animes = svc.get_all_anime()
        mangas = svc.get_all_manga()

        self.listbox.insert(tk.END, "My Anime List")
        self.listbox.insert(tk.END, "")
        for anime in animes:
            anime_id, title, year, seasons, rating, owned = anime

            # Format for display
            display_text = f"{anime_id} - {title} ({year}) | {seasons} seasons | {rating} rating | is owned: {owned}"

            # Insert into listbox
            self.listbox.insert(tk.END, display_text)

        self.listbox.insert(tk.END, "")
        self.listbox.insert(tk.END, "My Manga List")
        self.listbox.insert(tk.END, "")
        for manga in mangas:
            manga_id, title, author, illustrator, year, chapters, rating, owned = manga

            # Format for display
            display_text = f"{manga_id} - {title} ({year}) | by {author} | illustrations by {illustrator} | {chapters} seasons | {rating} rating | is owned: {owned}"

            # Insert into listbox
            self.listbox.insert(tk.END, display_text)


if __name__ == "__main__":
    root = tk.Tk()
    app = AnimeToMangaUI(root)
    root.mainloop()