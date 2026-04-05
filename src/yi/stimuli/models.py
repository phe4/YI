"""Stimulus models."""

from pydantic import BaseModel


class Stimulus(BaseModel):
    """External or internal event that may trigger cognition."""

    kind: str
    payload: dict


async def collect_stimuli() -> list[Stimulus]:
    """Collect pending stimuli.

    TODO: Pull from queues, timers, and internal event sources.
    """
    return []
