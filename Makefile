PYTHON ?= python3

.PHONY: verify
verify:
	$(PYTHON) -B -m unittest discover -v
	$(PYTHON) schema_drift_watch.py sample_schemas.csv

.PHONY: replay
replay:
	$(PYTHON) tools/replay_examples.py --report reports/replay.md
.PHONY: lint security check
lint:
	$(PYTHON) -m ruff check --config ruff.toml --no-cache .

security:
	$(PYTHON) -m bandit -q -ll -ii -r . -x ./.venv,./.git

check: verify lint security replay
