# Stream Schema Drift Watch architecture

Compares current event schemas against expected contracts and flags drift before AI features break.

```mermaid
flowchart LR
    N0["sample_schemas.csv"]
    N1["schema_drift_watch.py"]
    N2["parse fields / drift / drift report"]
    N3["Result for operator review"]
    N0 --> N1 --> N2 --> N3
```

## Operational boundaries

The documented run evaluates the bundled sample locally. Results depend on the quality and scope of the input. The demo makes no live infrastructure changes.
