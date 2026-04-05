"""Async runtime engine skeleton."""

from dataclasses import dataclass


@dataclass(slots=True)
class RuntimeEngine:
    """Coordinates periodic cognition ticks.

    TODO: Wire stimuli intake, state updates, memory writes, and action dispatch.
    """

    is_running: bool = False

    async def start(self) -> None:
        """Start the runtime loop."""
        self.is_running = True

    async def stop(self) -> None:
        """Stop the runtime loop."""
        self.is_running = False
