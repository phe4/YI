"""SQLite connection helper placeholders."""

from pathlib import Path


def database_path() -> Path:
    """Return default SQLite file path.

    TODO: Pull from configurable settings.
    """
    return Path("yi.db")
