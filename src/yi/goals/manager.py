"""Goal domain models and basic retrieval interfaces."""

from __future__ import annotations

from datetime import datetime

from pydantic import BaseModel, Field

from yi.models import GoalCategory, GoalStatus, new_id, utc_now


class Goal(BaseModel):
    """A durable objective tracked by the runtime over time."""

    id: str = Field(default_factory=new_id)
    name: str = Field(min_length=1, max_length=120)
    description: str = Field(default="", max_length=2000)
    category: GoalCategory = GoalCategory.PERSISTENT
    priority: float = Field(default=0.5, ge=0.0, le=1.0)
    tension: float = Field(default=0.2, ge=0.0, le=1.0)
    status: GoalStatus = GoalStatus.ACTIVE
    created_at: datetime = Field(default_factory=utc_now)
    updated_at: datetime = Field(default_factory=utc_now)


def active_goals() -> list[Goal]:
    """Return active goals.

    TODO: Pull goals from memory/db and rank dynamically.
    """
    return []
