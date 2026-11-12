# Stream Schema Drift Watch architecture

Compares current event schemas against expected contracts and flags drift before AI features break.

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

## Operational boundaries

The documented run evaluates the bundled sample locally. Results depend on the quality and scope of the input. The demo makes no live infrastructure changes.
