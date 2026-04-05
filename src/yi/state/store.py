"""In-memory and persisted state holders."""

from dataclasses import dataclass, field


@dataclass(slots=True)
class CognitiveState:
    """Mutable runtime state."""

    mode: str = "idle"
    attributes: dict[str, str] = field(default_factory=dict)
