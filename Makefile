.PHONY: setup test docker-test spec-check lint

setup:
	uv sync --all-extras --dev

test:
	uv run pytest tests/

docker-test:
	docker build --target builder -t chimera:test .
	docker run --rm chimera:test uv run pytest tests/

spec-check:
	@echo "Manual spec alignment check (future: add script)"
	@find specs/ -type f -name "*.md" -exec grep -L "ratified" {} \; || echo "All specs appear ratified"

lint:
	uv run ruff check .