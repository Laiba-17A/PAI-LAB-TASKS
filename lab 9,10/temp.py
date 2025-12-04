import pandas as pd
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt

df = pd.read_csv("Mall_Customers.csv")

X = df[["Annual Income (k$)","Spending Score (1-100)"]]

kmeans = KMeans(n_clusters=3, random_state=42)
df["Cluster"] = kmeans.fit_predict(X)

plt.scatter(df["Annual Income (k$)"], df["Spending Score (1-100)"], c=df["Cluster"], s=100)
plt.xlabel("annual income (k$)")
plt.ylabel("spending score (1-100)")
plt.title("customer segmentation (k-means)")
plt.show()

print("cluster assignments:")
print(df[["CustomerID","Cluster"]])
