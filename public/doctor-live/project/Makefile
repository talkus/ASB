.PHONY: dev lint test

dev:
	python -m pip install -e ".[dev]"

lint:
	ruff check . --fix
	ruff format .

test:
	pytest
