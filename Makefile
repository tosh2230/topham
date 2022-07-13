lint:
	poetry run flake8 src tests
	poetry run isort --check --diff src tests
	poetry run black --check src tests
type-check:
	poetry run mypy .
format:
	poetry run isort src tests
	poetry run black src tests
test:
	@poetry run pytest tests -v --cov=src
