"""Application entrypoint for YI."""

from fastapi import FastAPI

from yi.api.router import api_router
from yi.runtime.lifecycle import lifespan


def create_app() -> FastAPI:
    """Create and configure the FastAPI application."""
    app = FastAPI(title="YI", version="0.1.0", lifespan=lifespan)
    app.include_router(api_router)
    return app


app = create_app()
