
import pandas as pd 
import matplotlib.pyplot as plt

data = pd.read_csv('Mobile Reviews Sentiment - Mobile Reviews Sentiment.csv')
df=data.copy()
print(df.columns)

avg_rat = data.groupby('brand')['rating'].mean().reset_index()
plt.figure(figsize=(10, 6))
plt.bar(avg_rat['brand'], avg_rat['rating'], color='skyblue')
plt.xlabel('mobile brand')
plt.ylabel('average overall rating')
plt.title('average overall rating for each brand')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

