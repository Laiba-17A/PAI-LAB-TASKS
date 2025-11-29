import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("Mobile Reviews Sentiment - Mobile Reviews Sentiment.csv")

data['brand'] = data['brand'].str.lower()

avg_price = data.groupby('brand')['price_usd'].mean().reset_index()

print(avg_price)

plt.figure(figsize=(10, 6))
plt.bar(avg_price['brand'], avg_price['price_usd'])
plt.xlabel('mobile brand')
plt.ylabel('average price (usd)')
plt.title('average price (usd) for each brand')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
