import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("Mobile Reviews Sentiment - Mobile Reviews Sentiment.csv")

bins = [0.5, 1.5, 2.5, 3.5, 4.5, 5.5]
plt.hist(df['rating'], bins=bins, color='skyblue', edgecolor='black', rwidth=0.8)
plt.xticks(range(1, 6))
plt.title('rating distribution', fontsize=14)
plt.xlabel('rating', fontsize=12)
plt.ylabel('number of reviews', fontsize=12)
plt.tight_layout()
plt.show()
