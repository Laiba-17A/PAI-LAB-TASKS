import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("Mobile Reviews Sentiment - Mobile Reviews Sentiment.csv")

sentiment_counts = df['sentiment'].value_counts()

plt.pie(sentiment_counts, labels=sentiment_counts.index.str.lower(), autopct='%1.1f%%', colors=['lightgreen','lightcoral','lightskyblue'])
plt.title('sentiment distribution', fontsize=14)
plt.tight_layout()
plt.show()
