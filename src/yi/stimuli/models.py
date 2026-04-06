"""Stimulus domain models."""

from __future__ import annotations

from datetime import datetime

from pydantic import BaseModel, Field

from yi.models import StimulusSource, StimulusType, new_id, utc_now


class Stimulus(BaseModel):
    """An event that can trigger or modulate YI cognition.

    Stimuli can come from user interactions, the environment/timers, or internal
    subsystem events. Scoring fields (priority/novelty/urgency) are normalized
    into [0.0, 1.0] to keep decision policy math straightforward.
    """

    id: str = Field(default_factory=new_id)
    type: StimulusType
    source: StimulusSource
    timestamp: datetime = Field(default_factory=utc_now)
    content: dict[str, object] = Field(default_factory=dict)
    priority: float = Field(default=0.5, ge=0.0, le=1.0)
    novelty: float = Field(default=0.5, ge=0.0, le=1.0)
    urgency: float = Field(default=0.5, ge=0.0, le=1.0)
    related_context: list[str] = Field(default_factory=list)
    processable: bool = True


async def collect_stimuli() -> list[Stimulus]:
    """Collect pending stimuli from ingress adapters.

    TODO: Pull from user input queue, scheduled events, and internal runtime bus.
    """
    return []
