import pandas as pd
from sklearn.datasets import load_wine
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt
import numpy as np

data = load_wine()
wine = pd.DataFrame(data.data, columns=data.feature_names)

X = wine[['alcohol', 'total_phenols']]

scale = StandardScaler()
scale.fit(X)
X_scaled = scale.transform(X)

from sklearn.cluster import KMeans
kmeans = KMeans(n_clusters=4)
kmeans.fit(X_scaled)
y_pred = kmeans.predict(X_scaled)
print(y_pred)
print(kmeans.cluster_centers_)

newX = np.array([[13, 2.5]])
newXscaled = scale.transform(newX)
print("\n" + str(newXscaled))
print(kmeans.predict(newXscaled))

plt.scatter(X_scaled[:,0], X_scaled[:,1], c = y_pred)
plt.scatter(kmeans.cluster_centers_[:,0], kmeans.cluster_centers_[:,1],
            marker = "*", s =250, c = [0,1,2,3], edgecolors='k')
plt.xlabel('alcohol');plt.ylabel('total phenols')
plt.title('k-means (k=3)')
plt.show()
