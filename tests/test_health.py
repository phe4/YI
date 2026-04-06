from fastapi.testclient import TestClient

from yi.main import create_app


def test_health_endpoint_reports_runtime_running() -> None:
    app = create_app()

    with TestClient(app) as client:
        response = client.get("/health/")

    assert response.status_code == 200
    assert response.json() == {"status": "ok", "runtime": "running"}
