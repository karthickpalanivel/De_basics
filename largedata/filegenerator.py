import csv
import random
import string

# Generate random strings
def random_string(length=6):
    return ''.join(random.choices(string.ascii_uppercase + string.digits, k=length))

# Constants
NUM_RECORDS = 10

# Data storage
customer_bank_data = []
customer_details_data = []
credit_card_data = []
debit_card_data = []

# Create data
for i in range(1, NUM_RECORDS + 1):
    customer_id = f"CUST{i:03d}"
    account_number = 100000 + i
    IFSC = f"IFSC{random.randint(1000, 9999)}"
    branch_name = f"Branch_{random.choice(['A', 'B', 'C'])}"
    city = random.choice(['Mumbai', 'Delhi', 'Bangalore', 'Chennai', 'Kolkata'])
    pincode = f"{random.randint(100000, 999999)}"

    customer_bank_data.append([customer_id, account_number, IFSC, branch_name, city, pincode])

    cname = f"Customer_{i}"
    cphone = random.randint(9000000000, 9999999999)
    caddress = f"{random.randint(100, 999)} Street, {city}"
    ccity = city
    cpincode = int(pincode)
    cstate = random.choice(['MH', 'DL', 'KA', 'TN', 'WB'])
    ccountry = "India"
    nri = random.choice([True, False])

    customer_details_data.append([customer_id, cname, cphone, caddress, ccity, cpincode, cstate, ccountry, nri])

    cc_number = 4000000000000000 + i
    cc_type = random.choice(['Visa', 'MasterCard'])
    cc_category = random.choice(['Platinum', 'Gold', 'Silver'])

    credit_card_data.append([account_number, cc_number, cc_type, cc_category])

    dc_number = 5000000000000000 + i
    dc_type = random.choice(['Visa', 'RuPay'])
    dc_category = random.choice(['Premium', 'Classic'])

    debit_card_data.append([account_number, dc_number, dc_type, dc_category])

# Write CSV files
with open("customer_bank.csv", "w", newline='') as f:
    writer = csv.writer(f)
    writer.writerow(["customer_id", "account_number", "IFSC", "branch_name", "city", "pincode"])
    writer.writerows(customer_bank_data)

with open("customer_details.csv", "w", newline='') as f:
    writer = csv.writer(f)
    writer.writerow(["cus_id", "cname", "cphone", "caddress", "ccity", "cpincode", "cstate", "ccountry", "nri"])
    writer.writerows(customer_details_data)

with open("credit_card.csv", "w", newline='') as f:
    writer = csv.writer(f)
    writer.writerow(["cus_acc_number", "cc_number", "cc_type", "cc_category"])
    writer.writerows(credit_card_data)

with open("debit_card.csv", "w", newline='') as f:
    writer = csv.writer(f)
    writer.writerow(["dc_acc_number", "dc_number", "dc_type", "dc_category"])
    writer.writerows(debit_card_data)
