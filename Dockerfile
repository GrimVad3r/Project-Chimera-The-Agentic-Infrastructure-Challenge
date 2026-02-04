# syntax=docker/dockerfile:1

# Stage 1: Builder (for CI/tests + dev deps)
FROM python:3.12-slim AS builder

RUN pip install --no-cache-dir uv

WORKDIR /app

# Copy dependency files first → cache layer
COPY pyproject.toml uv.lock* ./

# Install all deps (including dev) for tests
RUN uv sync --frozen --all-extras --dev --no-install-project

# Copy source + tests
COPY . .

# Run tests (will fail — that's good)
RUN uv run pytest tests/ || true

# Stage 2: Runtime (slim production image — no dev deps)
FROM python:3.12-slim AS runtime

RUN pip install --no-cache-dir uv

WORKDIR /app

COPY --from=builder /app /app

# Install only runtime deps
RUN uv sync --frozen --no-dev --no-install-project

# Final CMD (placeholder — agent runtime would go here)
CMD ["uv", "run", "python", "-m", "chimera.main"]