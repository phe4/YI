"""Structured internal state model for YI runtime."""

from pydantic import BaseModel, Field

from yi.models import RuntimeMode


class InternalState(BaseModel):
    """Inspectable cognitive state used by the runtime and decision layers.

    Most fields are normalized [0,1] values so they can be combined and traced
    consistently during decision scoring.
    """

    attention_focus: str = "none"
    activation_level: float = Field(default=0.4, ge=0.0, le=1.0)
    fatigue: float = Field(default=0.1, ge=0.0, le=1.0)
    curiosity: float = Field(default=0.6, ge=0.0, le=1.0)
    stability: float = Field(default=0.8, ge=0.0, le=1.0)
    user_alignment: float = Field(default=0.7, ge=0.0, le=1.0)
    pending_tension: float = Field(default=0.2, ge=0.0, le=1.0)
    memory_pressure: float = Field(default=0.2, ge=0.0, le=1.0)
    reflection_need: float = Field(default=0.2, ge=0.0, le=1.0)
    runtime_mode: RuntimeMode = RuntimeMode.IDLE
