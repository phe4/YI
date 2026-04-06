from datetime import timedelta

import pytest

from yi.decision.policy import ActionDecision
from yi.goals.manager import Goal
from yi.iching.guidance import IChingSession
from yi.memory.store import MemoryRecord
from yi.models import GoalCategory, GoalStatus, MemoryType, StimulusSource, utc_now


def test_goal_rejects_updated_before_created() -> None:
    created_at = utc_now()
    with pytest.raises(ValueError):
        Goal(
            name="Stay aligned",
            category=GoalCategory.PERSISTENT,
            status=GoalStatus.ACTIVE,
            created_at=created_at,
            updated_at=created_at - timedelta(seconds=1),
        )


def test_memory_record_deduplicates_linked_memories() -> None:
    record = MemoryRecord(
        memory_type=MemoryType.EPISODIC,
        source=StimulusSource.USER,
        linked_memories=["m1", "m1", "m2"],
    )
    assert record.linked_memories == ["m1", "m2"]


def test_iching_session_normalizes_changing_lines() -> None:
    session = IChingSession(
        input_seed="seed",
        base_symbol="䷀",
        transformed_symbol="䷀",
        changing_lines=[6, 1, 6],
    )
    assert session.changing_lines == [1, 6]


def test_action_decision_rejects_blank_breakdown_key() -> None:
    with pytest.raises(ValueError):
        ActionDecision(selected_action="noop", score_breakdown={"": 0.1})
