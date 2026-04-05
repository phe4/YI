"""Decision policy placeholder."""

from yi.goals.manager import Goal
from yi.stimuli.models import Stimulus


async def choose_next_action(stimuli: list[Stimulus], goals: list[Goal]) -> str | None:
    """Choose an action identifier.

    TODO: Combine stimuli + state + memory + goals into scored decisions.
    """
    if not stimuli or not goals:
        return None
    return "noop"
