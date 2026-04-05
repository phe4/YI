"""Decision models and policy placeholder."""

from __future__ import annotations

from datetime import datetime

from pydantic import BaseModel, Field

from yi.goals.manager import Goal
from yi.models import utc_now
from yi.stimuli.models import Stimulus


class ActionDecision(BaseModel):
    """Represents a scored choice produced by the decision system."""

    selected_action: str
    reason_summary: str = Field(default="", max_length=2000)
    confidence: float = Field(default=0.5, ge=0.0, le=1.0)
    expected_cost: float = Field(default=0.0, ge=0.0)
    expected_value: float = Field(default=0.0)
    score_breakdown: dict[str, float] = Field(default_factory=dict)
    created_at: datetime = Field(default_factory=utc_now)


async def choose_next_action(stimuli: list[Stimulus], goals: list[Goal]) -> ActionDecision | None:
    """Choose the next action candidate.

    TODO: Combine stimuli + state + memory + goals into scored decisions.
    """
    if not stimuli or not goals:
        return None

    return ActionDecision(
        selected_action="noop",
        reason_summary="Placeholder: no policy configured yet.",
        confidence=0.1,
        score_breakdown={"baseline": 0.1},
    )
