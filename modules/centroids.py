import numpy as np

def count_centroid(cluster_X_val, cluster_Y_val, cluster_Z_val):
    x_centroid = np.sum(cluster_X_val) / len(cluster_X_val)
    y_centroid = np.sum(cluster_Y_val) / len(cluster_Y_val)
    z_centroid = np.sum(cluster_Z_val) / len(cluster_Z_val)
    return (x_centroid, y_centroid, z_centroid)