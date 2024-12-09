import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv('raw-data\benin-malanville.csv')

summary_stats = df.describe()
print(summary_stats)

df['Timestamp'] = pd.to_datetime(df['Timestamp'])
df.set_index('Timestamp', inplace=True)
df['GHI'].plot(figsize=(10, 6))
plt.title('GHI over Time')
plt.show()