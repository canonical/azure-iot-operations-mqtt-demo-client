.PHONY: lint-check
lint-check:
	ruff check src/

.PHONY: lint-fix
lint-fix:
	ruff check --fix src/

.PHONY: format-check
format-check:
	ruff format --check src/

.PHONY: format-fix
format-fix:
	ruff format src/

.PHONY: depends-dev
depends-dev:
	pip install -r requirements-dev.txt
