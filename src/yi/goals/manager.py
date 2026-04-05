"""Goal evaluation placeholder."""

from dataclasses import dataclass


@dataclass(slots=True)
class Goal:
    """A durable objective for YI."""

    name: str
    priority: int = 0


def active_goals() -> list[Goal]:
    """Return active goals.

    TODO: Pull goals from memory/db and rank dynamically.
    """
    return []
