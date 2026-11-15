# Skills and verification

## What this repository demonstrates

A stream contract comparison that checks expected field names against current fields and reported required-field gaps. Missing fields block the change, and added fields go to review.

## Reproduce the result

The purchase event schema is blocked. The device event schema has additions and goes to review. Reproduce the primary fixture with `python3 schema_drift_watch.py sample_schemas.csv`.

Run `make verify` locally. Ruff and Bandit medium/high checks passed for the checked Python code.

## Scope

The comparison covers field sets and supplied required-field counts. Validate types and compatibility with the actual schema registry separately.

Treat missing required fields as a contract issue. Review additive changes with downstream consumers before approving them.

[schema_drift_watch.py](../schema_drift_watch.py) · [examples/Demo 1.stdout.txt](../examples/Demo%201.stdout.txt) · [Architecture](../docs/ARCHITECTURE.md) · [Case study](../docs/CASE_STUDY.md) · [Runbook](../docs/RUNBOOK.md) · [CI template](../docs/github-actions/ci.yml)
