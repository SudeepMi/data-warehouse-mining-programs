#Hierarchical Clustering (Agglomerative Clustering)

#Agglomerative Clustering

import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import AgglomerativeClustering
from scipy.cluster import hierarchy

x = [4, 5, 10, 4, 3, 11, 14 , 6, 10, 12]
y = [21, 19, 24, 17, 16, 25, 24, 22, 21, 21]

data = list(zip(x, y))

hierarchical_cluster = AgglomerativeClustering(n_clusters=2, metric='euclidean', linkage='single')
labels = hierarchical_cluster.fit_predict(data)

clusters = hierarchy.linkage(data, method="ward")
dendrogram = hierarchy.dendrogram(clusters)

"""
print(labels)

plt.scatter(x, y, c=labels)"""
plt.show()


