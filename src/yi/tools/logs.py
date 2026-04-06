"""Tool execution logging models."""

from __future__ import annotations

from datetime import datetime

from pydantic import BaseModel, Field

from yi.models import new_id, utc_now


class ToolCallLog(BaseModel):
    """Record of a tool execution attempt for inspectability."""

    id: str = Field(default_factory=new_id)
    tool_name: str = Field(min_length=1, max_length=120)
    trigger_reason: str = Field(default="", max_length=1000)
    input_payload: dict[str, object] = Field(default_factory=dict)
    output_payload: dict[str, object] = Field(default_factory=dict)
    success: bool = True
    usefulness_score: float = Field(default=0.5, ge=0.0, le=1.0)
    created_at: datetime = Field(default_factory=utc_now)
