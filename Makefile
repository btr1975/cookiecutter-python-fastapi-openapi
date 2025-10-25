# Makefile for project needs
# Author: Ben Trachtenberg
# Version: 1.0.1
#

.PHONY: all info coverage pytest black security pip-export

info:
	@echo "make options"
	@echo "    black     To format code with black"
	@echo "    coverage  To run coverage and display ASCII and output to htmlcov"
	@echo "    pytest    To run pytest with verbose option"

all: black pylint coverage security pip-export vulnerabilities

coverage:
	@uv run pytest --cov --cov-report=html -vvv

pytest:
	@uv run pytest --cov -vvv

pylint:
	@uv run pylint hooks/

black:
	@uv run black hooks/
	@uv run black tests/

security:
	@uv run bandit -c pyproject.toml -r .

vulnerabilities:
	@uv run pip-audit -r requirements.txt

pip-export:
	@uv export --no-dev --no-emit-project --no-editable > requirements.txt
	@uv export --no-emit-project --no-editable > requirements-dev.txt
