# Stream Schema Drift Watch

Compares current event schemas against expected contracts and flags drift before AI features break.

Focus: Kafka streams, schema drift, ML feature reliability, SRE.

Portfolio framing: Apple-scale client-style platform project using synthetic data only.

## Run

```bash
python3 schema_drift_watch.py sample_schemas.csv
```

## Verify

```bash
python3 -m unittest discover . -v
```

## Local verification

Run `make verify` with Make and Python 3 installed. The target runs the documented sample through the project CLI. It also runs the existing Python unit tests.

## Business problem

A changed event contract can silently remove fields required by downstream feature consumers. Reviewers need to distinguish breaking gaps from additive changes.

## Project walkthrough

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

[Architecture and data flow](docs/ARCHITECTURE.md) · [Business problem, demo, and verification](docs/CASE_STUDY.md)

## Run the project

### Local setup

Run `make verify` with Python 3 and Make installed.

### CLI usage

```sh
python3 schema_drift_watch.py sample_schemas.csv
```

### Replay usage

Run `make replay` to replay the checked-in inputs. The runner compares stdout with the baseline, reports differences, and exits nonzero on regression.

[Replay cases](examples/replay-manifest.json) · [Generated report](reports/replay.md) · [Rule implementation](docs/RULES.md)

### Run tests

[Verification report](reports/verification.md) · [Business problem, sample behavior, and limitations](docs/CASE_STUDY.md)


### Limitations

The verification report covers the bundled local examples. See the [case study](docs/CASE_STUDY.md) for project-specific assumptions and operating limits.
