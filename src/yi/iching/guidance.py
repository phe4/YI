"""I Ching experimental session models and placeholder derivation logic."""

from __future__ import annotations

from datetime import datetime

from pydantic import BaseModel, Field, field_validator

from yi.models import new_id, utc_now


class IChingSession(BaseModel):
    """Inspectable output for experimental I-Ching mode."""

    id: str = Field(default_factory=new_id)
    input_seed: str = Field(min_length=1, max_length=500)
    base_symbol: str = Field(min_length=1, max_length=16)
    changing_lines: list[int] = Field(default_factory=list)
    transformed_symbol: str = Field(min_length=1, max_length=16)
    interpretation: str = Field(default="", max_length=4000)
    suggestion: str = Field(default="", max_length=2000)
    created_at: datetime = Field(default_factory=utc_now)

    @field_validator("changing_lines")
    @classmethod
    def validate_changing_lines(cls, changing_lines: list[int]) -> list[int]:
        """Allow only classic line indexes 1..6 without duplicates."""
        if any(line < 1 or line > 6 for line in changing_lines):
            raise ValueError("changing_lines values must be between 1 and 6")
        deduped = sorted(set(changing_lines))
        return deduped


def derive_hexagram(seed: str) -> IChingSession:
    """Derive a symbolic I Ching session from an input seed.

    TODO: Implement deterministic, inspectable mapping from seed + state.
    """
    return IChingSession(
        input_seed=seed,
        base_symbol="䷀",
        changing_lines=[],
        transformed_symbol="䷀",
        interpretation="Placeholder interpretation.",
        suggestion="Observe current dynamics before acting.",
    )
