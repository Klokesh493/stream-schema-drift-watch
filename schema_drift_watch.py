import csv
import sys


def parse_fields(value):
    return {part.strip() for part in value.split(",") if part.strip()}


def drift(row):
    expected = parse_fields(row["expected_fields"])
    current = parse_fields(row["current_fields"])
    missing = expected - current
    added = current - expected
    severity = "ok"
    if int(row["required_missing"]) > 0 or missing:
        severity = "block"
    elif added:
        severity = "review"
    return {"topic": row["topic"], "missing": sorted(missing), "added": sorted(added), "severity": severity}


def drift_report(rows):
    return [drift(row) for row in rows if drift(row)["severity"] != "ok"]


def main(path):
    with open(path, newline="", encoding="utf-8") as handle:
        for item in drift_report(csv.DictReader(handle)):
            print(f'{item["severity"]}: {item["topic"]}')


if __name__ == "__main__":
    main(sys.argv[1])
