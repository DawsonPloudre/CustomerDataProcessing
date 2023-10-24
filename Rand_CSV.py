import pandas as pd
import random

# Create a list to store sample data
data = []

# Define income ranges and their corresponding minimum and maximum values
income_ranges = [
    "0-20000",
    "20001-40000",
    "40001-60000",
    "60001-80000",
    "80001-100000",
    "100000-1000000",
]

# Generate 100 customers
for customer_id in range(1, 101):
    age = random.randint(18, 70)
    gender = random.choice(['Male', 'Female'])
    purchases = random.randint(0, 10)
    income_range = random.choice(income_ranges)  # Randomly select an income range

    data.append([customer_id, age, gender, purchases, income_range])

# Create a DataFrame
columns = ['CustomerID', 'Age', 'Gender', 'Purchases', 'IncomeRange']
df = pd.DataFrame(data, columns=columns)

# Save the DataFrame as a CSV file
df.to_csv('customer_data.csv', index=False)
