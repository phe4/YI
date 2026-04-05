"""Memory domain models and persistence facade."""

from __future__ import annotations

from datetime import datetime

from pydantic import BaseModel, Field

from yi.models import MemoryType, StimulusSource, new_id, utc_now


class MemoryRecord(BaseModel):
    """A weighted memory unit used in retrieval and consolidation.

    `embedding` is intentionally left as optional metadata for future vector
    integration; no vector store infrastructure is implemented yet.
    """

    id: str = Field(default_factory=new_id)
    memory_type: MemoryType
    content: dict[str, object] = Field(default_factory=dict)
    importance: float = Field(default=0.5, ge=0.0, le=1.0)
    recency: float = Field(default=1.0, ge=0.0, le=1.0)
    frequency: int = Field(default=1, ge=1)
    confidence: float = Field(default=0.7, ge=0.0, le=1.0)
    source: StimulusSource = StimulusSource.SYSTEM
    linked_memories: list[str] = Field(default_factory=list)
    embedding: list[float] | None = None
    created_at: datetime = Field(default_factory=utc_now)
    updated_at: datetime = Field(default_factory=utc_now)


async def remember(record: MemoryRecord) -> None:
    """Persist a memory record.

    TODO: Write to SQLite and add retention policy.
    """
    _ = record
