"""Tool registration and lookup placeholder."""

from dataclasses import dataclass


@dataclass(slots=True)
class ToolSpec:
    """Metadata for callable tools."""

    name: str
    description: str


def list_tools() -> list[ToolSpec]:
    """Return registered tools.

    TODO: Add dynamic registration + capability filters.
    """
    return []
