"""FastAPI lifecycle integration for runtime startup/shutdown."""

from collections.abc import AsyncIterator
from contextlib import asynccontextmanager

from fastapi import FastAPI

from yi.runtime.engine import RuntimeEngine


@asynccontextmanager
async def lifespan(app: FastAPI) -> AsyncIterator[None]:
    """Bind runtime setup and teardown to FastAPI lifespan."""
    engine = RuntimeEngine()
    app.state.runtime_engine = engine

    await engine.start()
    try:
        yield
    finally:
        await engine.stop()
