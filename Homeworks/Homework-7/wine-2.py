import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from sklearn.datasets import load_wine
from sklearn.cluster import KMeans

data = load_wine()

X = data.data
y = data.target

df = pd.DataFrame(data.data, columns=data.feature_names)

print("Available columns:")
print(data.feature_names)

print(df.head())

# 1. Scatterplot of alochol vs. flavanoids
plt.scatter(df['alcohol'], df['flavanoids'])
plt.xlabel('alcohol')
plt.ylabel('flavanoids')
plt.show()

# 2. Prepare data for clustering (selected columns: alcohol, flavanoids)
X = df[['alcohol', 'flavanoids']].values

# 3. Run k-means clustering with n_clusters=3
kmeans = KMeans(n_clusters=3, random_state=0)
kmeans.fit(X)

# 4. Add cluster labels to the DataFrame
labels = kmeans.labels_
df['cluster'] = labels

# 5. Scatterplot colored by cluster labels
plt.scatter(df['alcohol'], df['flavanoids'], c=df['cluster'], cmap='viridis')
plt.xlabel("alcohol")
plt.ylabel("flavanoids")
plt.title("K-Means Clustering (k=3)")
plt.colorbar(label='Cluster')
plt.show()