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
