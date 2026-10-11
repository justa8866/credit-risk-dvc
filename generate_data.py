
import csv
import os
import random

os.makedirs("data", exist_ok=True)
random.seed(42)

with open("data/large_dataset.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerow(["client_id", "age", "income", "loan_amount", "credit_risk"])

    for i in range(3_200_000):
        age = random.randint(18, 75)
        income = random.randint(2000, 25000)
        loan = random.randint(5000, 500000)
        risk = int(loan > income * 12)

        writer.writerow([f"CLIENT_{i:010d}", age, income, loan, risk])

size_mb = os.path.getsize("data/large_dataset.csv") / 1024**2
print(f"Rozmiar datasetu: {size_mb:.2f} MB")
