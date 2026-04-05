"""Health endpoints."""

from fastapi import APIRouter, Request

router = APIRouter()


@router.get("/")
async def health(request: Request) -> dict[str, str]:
    """Return basic liveness data for the process and runtime."""
    engine = request.app.state.runtime_engine
    status = "running" if engine.is_running else "stopped"
    return {"status": "ok", "runtime": status}
