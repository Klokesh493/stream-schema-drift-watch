# Local verification

Command: `make verify`

Result: **PASS**

````text
python3 -B -m unittest discover -v
python3 schema_drift_watch.py sample_schemas.csv
block: events.purchase
review: events.device
test_blocks_missing_expected_field (test_schema_drift_watch.SchemaDriftWatchTest) ... ok
test_reviews_additive_field (test_schema_drift_watch.SchemaDriftWatchTest) ... ok

----------------------------------------------------------------------
Ran 2 tests in 0.000s

OK
````
