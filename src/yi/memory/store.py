"""Memory persistence facade."""

from dataclasses import dataclass


@dataclass(slots=True)
class MemoryRecord:
    """Single memory item."""

    key: str
    value: str


async def remember(record: MemoryRecord) -> None:
    """Persist a memory record.

    TODO: Write to SQLite and add retention policy.
    """
    _ = record
