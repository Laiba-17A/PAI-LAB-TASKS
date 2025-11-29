import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

df = pd.read_csv("Mobile Reviews Sentiment - Mobile Reviews Sentiment.csv")

df = df[pd.to_numeric(df['price_usd'], errors='coerce').notnull()]
df = df[pd.to_numeric(df['rating'], errors='coerce').notnull()]

df['price_usd'] = df['price_usd'].astype(float)
df['rating'] = df['rating'].astype(float)

mean_price = df['price_usd'].mean()
mean_rating = df['rating'].mean()

overpriced = df[(df['price_usd'] > mean_price) & (df['rating'] < mean_rating)]

plt.figure(figsize=(8,6))
plt.scatter(df['price_usd'], df['rating'] , color='skyblue', label='all models')
plt.scatter(overpriced['price_usd'], overpriced['rating'] , color='red', label='overpriced')
plt.ylabel('price_usd', fontsize=12)
plt.xlabel('rating', fontsize=12)
plt.title('overpriced models (high price, low rating)', fontsize=14)
plt.legend()
plt.tight_layout()
plt.show()
