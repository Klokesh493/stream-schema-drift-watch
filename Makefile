PYTHON ?= python3

.PHONY: verify
verify:
	$(PYTHON) -B -m unittest discover -v
	$(PYTHON) schema_drift_watch.py sample_schemas.csv

.PHONY: replay
replay:
	$(PYTHON) tools/replay_examples.py --report reports/replay.md
