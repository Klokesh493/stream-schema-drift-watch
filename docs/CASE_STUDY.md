# Stream Schema Drift Watch walkthrough

## Business problem

Compares current event schemas against expected contracts and flags drift before AI features break.

## Reproduce the workflow

Run `python3 schema_drift_watch.py sample_schemas.csv` from the repository root. Then run `make verify` to repeat the local checks.

Observed sample output

```text
block: events.purchase
review: events.device
```

The sample supplies these fields. `topic`, `expected_fields`, `current_fields`, `required_missing`.

## Verification

Sample command and local checks passed.

## Limitations

The documented run evaluates the bundled sample locally. Results depend on the quality and scope of the input. The demo makes no live infrastructure changes.
