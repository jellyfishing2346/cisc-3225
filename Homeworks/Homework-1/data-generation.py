import pandas as pd
import numpy as np
from datetime import datetime, timedelta

# 1. Setup parameters
np.random.seed(42)
n_rows = 100
categories = ['Mobile', 'Laptop', 'Tablet', 'Accessories']
regions = ['North', 'South', 'East', 'West']

# 2. Generate data
data = {
    'Date': [datetime(2025, 1, 1) + timedelta(days=np.random.randint(0, 365)) for _ in range(n_rows)],
    'Category': [np.random.choice(categories) for _ in range(n_rows)],
    'Region': [np.random.choice(regions) for _ in range(n_rows)],
    'Units Sold': np.random.randint(1, 15, n_rows),
    'Unit Price': np.random.uniform(50, 1200, n_rows).round(2),
    'Customer Rating': np.random.uniform(1, 5, n_rows).round(1) # For the Scatter Plot
}

df = pd.DataFrame(data).sort_values('Date')

# 3. Save to Excel
df.to_csv('Sales_Data_Assignment.csv', index=False)
print("Excel file 'Sales_Data_Assignment.csv' has been created.")