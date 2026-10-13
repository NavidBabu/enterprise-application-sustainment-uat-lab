import csv
from collections import Counter

# Example analysis script for exported issue data.
# Export the Issue Log worksheet to CSV as issue_log.csv before running.

with open("issue_log.csv", newline="") as f:
    rows = list(csv.DictReader(f))

print("Total issues:", len(rows))
print("By category:", Counter(r["Category"] for r in rows))
print("By severity:", Counter(r["Severity"] for r in rows))
print("By status:", Counter(r["Status"] for r in rows))

open_items = [r for r in rows if r["Status"] in {"Open", "In Progress"}]
print("Open / in-progress issues:", len(open_items))
