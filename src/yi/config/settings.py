"""Pydantic settings for YI runtime configuration."""

from pydantic import BaseModel


class Settings(BaseModel):
    """Basic application settings.

    TODO: Replace with BaseSettings + environment loading when configuration expands.
    """

    app_name: str = "YI"
    database_url: str = "sqlite:///./yi.db"
    tick_interval_seconds: float = 1.0
