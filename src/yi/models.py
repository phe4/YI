"""Shared model primitives for YI domain objects."""

from __future__ import annotations

from datetime import datetime, timezone
from enum import StrEnum
from uuid import uuid4


def utc_now() -> datetime:
    """Return a timezone-aware UTC timestamp."""
    return datetime.now(timezone.utc)


def new_id() -> str:
    """Generate a stable string identifier for domain records."""
    return str(uuid4())


class StimulusType(StrEnum):
    """Types of stimuli entering the cognitive loop."""

    USER_INPUT = "user_input"
    ENVIRONMENT_EVENT = "environment_event"
    INTERNAL_EVENT = "internal_event"


class StimulusSource(StrEnum):
    """Origin of a stimulus payload."""

    USER = "user"
    TIMER = "timer"
    SENSOR = "sensor"
    RUNTIME = "runtime"
    MEMORY = "memory"
    SYSTEM = "system"


class RuntimeMode(StrEnum):
    """High-level runtime mode for the continuously running agent."""

    ACTIVE = "active"
    IDLE = "idle"
    REFLECTING = "reflecting"
    SLEEPING = "sleeping"
    ERROR_RECOVERY = "error_recovery"


class GoalCategory(StrEnum):
    """Goal horizon categories."""

    IMMEDIATE = "immediate"
    PERSISTENT = "persistent"
    META = "meta"


class GoalStatus(StrEnum):
    """Lifecycle state for goals."""

    ACTIVE = "active"
    PAUSED = "paused"
    COMPLETED = "completed"
    DROPPED = "dropped"


class MemoryType(StrEnum):
    """Types of memory tracked by YI."""

    EPISODIC = "episodic"
    SEMANTIC = "semantic"
    WORKING = "working"
    PROCEDURAL = "procedural"
    REFLECTION = "reflection"


class ReflectionOutcome(StrEnum):
    """Possible outcomes after a reflection cycle."""

    CONSOLIDATED = "consolidated"
    REPRIORITIZED = "reprioritized"
    NO_CHANGE = "no_change"
    ESCALATED = "escalated"
