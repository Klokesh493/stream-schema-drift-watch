# Stream Schema Drift Watch

A changed event contract can silently remove fields required by downstream feature consumers. Reviewers need to distinguish breaking gaps from additive changes.

## What I built

I built a stream contract comparison that checks expected field names against current fields and reported required-field gaps. Missing fields block the change, and added fields go to review.

## How it works

```mermaid
flowchart LR
    A["Expected and current event field lists"]
    B["Compare field sets and required fields"]
    C{"Required field missing?"}
    D["Block schema change"]
    E["Review additions or omit unchanged schema"]
    A --> B --> C
    C -->|Yes| D
    C -->|No| E
```

[Architecture](docs/ARCHITECTURE.md) · [Decision rules and source](docs/RULES.md)

## Tools used

| Tool | Role in this repository |
| --- | --- |
| Python | [schema_drift_watch.py](schema_drift_watch.py) implements the CLI and decision rules. Uses `csv` to read tabular exports. |
| Make | Runs the documented example and the local `unittest` suite. |
| Python replay runner | Compares actual stdout with the checked-in baseline fixtures. |
| Ruff and Bandit | Developer lint and static security checks through `make check`. |

## Run the project

Use Python 3.10+ and Make. From the repository root:

```sh
python3 schema_drift_watch.py sample_schemas.csv
```

The purchase event schema is blocked. The device event schema has additions and goes to review. [Full expected output](examples/Demo%201.stdout.txt)

### Additional replay cases

- **Last sample record in isolation** · `python3 schema_drift_watch.py examples/last-record.csv` · [Expected output](examples/Last%20sample%20record%20in%20isolation.stdout.txt)

## Verify the project

```sh
make verify
make replay
```

`make replay` checks the recorded cases and exits nonzero if the output changes.
See the [developer guide](docs/DEVELOPMENT.md) for the pinned lint and security tools.

## Operating limits

The comparison covers field sets and supplied required-field counts. Validate types and compatibility with the actual schema registry separately.

[Case study](docs/CASE_STUDY.md) · [Operator runbook](docs/RUNBOOK.md) · [Verification report](reports/verification.md)
