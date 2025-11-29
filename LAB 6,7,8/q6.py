import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('mobile reviews sentiment - mobile reviews sentiment.csv')
df['rating'] = pd.to_numeric(df['rating'], errors='coerce').fillna(0).astype(int)
df = df[df['rating'].between(1, 5)]

sent = ['Negative', 'Neutral', 'Positive']
data = [df[df['sentiment'] == s]['rating'] for s in sent]
colors = ['red', 'yellow', 'green']

fig, ax = plt.subplots(figsize=(10, 6))
box = ax.boxplot(data, tick_labels=sent, patch_artist=True, medianprops={'color': 'black'})

for p, c in zip(box['boxes'], colors):
    p.set_facecolor(c)
    p.set_edgecolor('black')

ax.set_title('sentiment vs rating')
ax.set_xlabel('sentiment')
ax.set_ylabel('rating')
ax.set_yticks(range(1, 6))
ax.set_ylim(0.5, 5.5)
ax.grid(axis='y', linestyle='--', alpha=0.7)

plt.show()
