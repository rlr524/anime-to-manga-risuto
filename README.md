# AnimeToManga Risuto
### ("Anime and Manga List" in Japanese)

A small Python app to manage personal anime and manga entries using simple dataclasses, a service layer that 
performs CRUD against a database, and a Tkinter UI. This README was bootstrapped with GitHub Copilot.

## Files
- `models.py` — domain dataclasses: `Anime`, `Manga`
- `services.py` — DB CRUD and validation functions
- `ui.py` — Tkinter user interface (`AnimeToMangaUI`) that uses the services

## Models
- `Anime` fields: `id`, `title`, `year`, `seasons`, `rating`, `owned`, `notes`
- `Manga` fields: `id`, `title`, `author`, `illustrator`, `year`, `chapters`, `rating`, `owned`, `notes`

## Services
Key functions:
- `get_anime(anime_id)`, `get_manga(manga_id)` — fetch single record
- `get_all_anime()`, `get_all_manga()` — fetch all records
- `add_anime(anime)`, `add_manga(manga)` — insert with validation and transaction handling
- `delete_anime(anime_id)`, `delete_manga(manga_id)` — hard delete
- `validate_anime_data(...)`, `validate_manga_data(...)` — simple field validation

Notes: `services.py` uses a `Database` connection (imported from `database`) and returns DB rows as tuples.

## UI
- `AnimeToMangaUI` (in `ui.py`) provides:
  - Menu and buttons for add/view/delete/refresh
  - List view showing anime and manga entries
  - Popups for adding and viewing details
  - Uses the functions from `services.py` to interact with the database

## Running
- Ensure a working `database` module / SQLite DB is available (as used by `services.py`).
- Start the UI with:
  - `python ui.py`

## Notes
- This README is based only on `models.py`, `services.py`, and `ui.py`.
- Data returned from services are DB rows (tuples); UI code expects tuple unpacking when displaying details.



