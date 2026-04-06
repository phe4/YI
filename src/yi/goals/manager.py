"""Goal domain models and basic retrieval interfaces."""

from __future__ import annotations

from datetime import datetime

from pydantic import BaseModel, Field, model_validator

from yi.models import GoalCategory, GoalStatus, new_id, utc_now


class Goal(BaseModel):
    """A durable objective tracked by the runtime over time.

    `updated_at` is constrained to be >= `created_at` so timeline ordering stays
    inspectable when serialized or persisted later.
    """

    id: str = Field(default_factory=new_id)
    name: str = Field(min_length=1, max_length=120)
    description: str = Field(default="", max_length=2000)
    category: GoalCategory = GoalCategory.PERSISTENT
    priority: float = Field(default=0.5, ge=0.0, le=1.0)
    tension: float = Field(default=0.2, ge=0.0, le=1.0)
    status: GoalStatus = GoalStatus.ACTIVE
    created_at: datetime = Field(default_factory=utc_now)
    updated_at: datetime = Field(default_factory=utc_now)

    @model_validator(mode="after")
    def validate_timestamps(self) -> "Goal":
        """Ensure update timestamps do not predate creation."""
        if self.updated_at < self.created_at:
            raise ValueError("updated_at must be greater than or equal to created_at")
        return self


def active_goals() -> list[Goal]:
    """Return active goals.

    TODO: Pull goals from memory/db and rank dynamically.
    """
    return []
