import math
import os
import matplotlib.pyplot as plt
import seaborn as sns

def draw_clusters_scatterplot(cluster_0, cluster_1, cluster_2, cluster_3):
    fig = plt.figure(figsize=(6,7))
    ax = plt.axes(projection = '3d')

    ax.scatter(cluster_0[0], cluster_0[1], cluster_0[2], alpha=0.8, c='red', label="Cluster 0")
    ax.scatter(cluster_1[0], cluster_1[1], cluster_1[2], alpha=0.8, c='green', label="Cluster 1")
    ax.scatter(cluster_2[0], cluster_2[1], cluster_2[2], alpha=0.8, c='blue', label="Cluster 2")
    ax.scatter(cluster_3[0], cluster_3[1], cluster_3[2], alpha=0.8, c='yellow', label="Cluster 3")

    plt.title("Clustering results")
    plt.legend(loc=2)

    plt.show()