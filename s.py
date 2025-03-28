import pandas as pd
import numpy as np
from datetime import datetime, timedelta


np.random.seed(42)


num_entries = np.random.randint(400, 501)


start_date = datetime(2020, 1, 1)
end_date = datetime(2023, 12, 31)
date_range = (end_date - start_date).days
dates = [start_date + timedelta(days=np.random.randint(0, date_range)) for _ in range(num_entries)]


feature1 = np.random.uniform(10, 100, num_entries)
feature2 = np.random.uniform(20, 150, num_entries)


prices = 2 * feature1 + 1.5 * feature2 + np.random.normal(0, 20, num_entries)


data = pd.DataFrame({
    'Date': dates,
    'Feature1': feature1,
    'Feature2': feature2,
    'Price': prices
})


data = data.sample(frac=1).reset_index(drop=True)


data.to_csv('agriculture_commodities.csv', index=False)

print(f"Sample data generated with {num_entries} entries and saved to 'agriculture_commodities.csv'")
