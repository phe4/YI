"""Reflection/consolidation event models."""

from __future__ import annotations

from datetime import datetime

from pydantic import BaseModel, Field

from yi.models import ReflectionOutcome, new_id, utc_now


class ReflectionLog(BaseModel):
    """Captures introspection and memory consolidation events."""

    id: str = Field(default_factory=new_id)
    trigger: str = Field(min_length=1, max_length=200)
    summary: str = Field(default="", max_length=2000)
    affected_memory_ids: list[str] = Field(default_factory=list)
    outcome: ReflectionOutcome = ReflectionOutcome.NO_CHANGE
    created_at: datetime = Field(default_factory=utc_now)
