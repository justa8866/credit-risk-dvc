
import csv

with open("data/large_dataset.csv", "a", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerow(["CLIENT_NEW_001", 35, 8500, 120000, 1])

print("Dataset updated successfully.")
