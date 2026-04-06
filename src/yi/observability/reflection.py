"""Reflection/consolidation event models."""

from __future__ import annotations

from datetime import datetime

from pydantic import BaseModel, Field, field_validator

from yi.models import ReflectionOutcome, new_id, utc_now


class ReflectionLog(BaseModel):
    """Captures introspection and memory consolidation events."""

    id: str = Field(default_factory=new_id)
    trigger: str = Field(min_length=1, max_length=200)
    summary: str = Field(default="", max_length=2000)
    affected_memory_ids: list[str] = Field(default_factory=list)
    outcome: ReflectionOutcome = ReflectionOutcome.NO_CHANGE
    created_at: datetime = Field(default_factory=utc_now)

    @field_validator("affected_memory_ids")
    @classmethod
    def dedupe_memory_ids(cls, affected_memory_ids: list[str]) -> list[str]:
        """Keep affected memory IDs unique while preserving order."""
        seen: set[str] = set()
        deduped: list[str] = []
        for memory_id in affected_memory_ids:
            if memory_id not in seen:
                seen.add(memory_id)
                deduped.append(memory_id)
        return deduped
