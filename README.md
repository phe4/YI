# YI

YI is a prototype for a continuously running, stimulus-driven cognitive system for a single user.

This repository currently contains the **initial architecture skeleton** only.

## Project Structure

```text
src/yi/
  actions/        # Action execution interfaces
  api/            # FastAPI routers and HTTP endpoints
  config/         # Runtime/configuration models
  db/             # SQLite boundary and persistence plumbing
  decision/       # Decision policy and planners
  goals/          # Goal definitions and management
  iching/         # I Ching-inspired symbolic guidance modules
  memory/         # Memory data model + persistence facade
  observability/  # Logging, metrics, tracing placeholders
  runtime/        # Runtime engine and lifecycle integration
  state/          # Cognitive state models/store
  stimuli/        # Stimulus ingestion and event models
  tools/          # Tool definitions and registry
tests/            # Test suite
```

## Requirements

- Python 3.11+
- pip

## Setup

```bash
python -m venv .venv
source .venv/bin/activate
pip install -e .[dev]
```

## Run the API

```bash
uvicorn yi.main:app --reload
```

Then open:
- `http://127.0.0.1:8000/health/`

## Run tests

```bash
pytest
```

## Notes

- Most modules intentionally contain placeholders and TODO comments.
- Business logic is not implemented yet by design.
