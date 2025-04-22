import csv
import random
from datetime import datetime, timedelta

# Sample data
locations = ["New York", "Chicago", "Los Angeles", "Houston"]
base_date = datetime(2023, 1, 1)

# Generate 100 records
records = []
for i in range(1, 101):
    order_id = i
    customer_id = random.randint(1000, 9999)
    amount = random.randint(50, 500)
    order_date = base_date + timedelta(days=random.randint(0, 365))
    order_date_str = order_date.strftime("%Y-%m-%d")
    location = random.choice(locations)
    records.append([order_id, customer_id, amount, order_date_str, location])

# Write to text file (CSV format)
with open(r"D:\\coding\\PySpark\\rawData\\orders.txt", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["order_id", "customer_id", "amount", "order_date", "location"])  # Header
    writer.writerows(records)

print("orders.txt created with 100 records")