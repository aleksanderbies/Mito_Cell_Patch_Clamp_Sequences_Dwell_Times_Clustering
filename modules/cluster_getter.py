import numpy as np
import pandas as pd

from modules.centroids import count_centroid

def get_all_clusters(values, cluster_no):
    clusters = [ [] for i in range(cluster_no) ]
    for i in values:
        for j in range(cluster_no):
            if i[3] == j:
                clusters[j].append(i)
    return clusters

def delete_target_column(clusters):
    for i in range(len(clusters)):
        clusters[i] = np.delete(clusters[i], 3, axis=1)
    return clusters

def get_X_Y_Z_from_cluster(cluster):
    return cluster[:, 0], cluster[:, 1], cluster[:, 2]

def check_cluster_elements(cluster, centroid, corr_to_check):
    indices_to_remove = []
    new_centroid = centroid
    for i in range(len(cluster)):

        corr = np.corrcoef(cluster[i], centroid)[0][1]

        if(corr < corr_to_check):
            indices_to_remove.append(i)
            this_cluster = np.copy(cluster)
            this_cluster = np.delete(this_cluster, indices_to_remove, axis=0)
            c_x, c_y, c_z = get_X_Y_Z_from_cluster(this_cluster)
            new_centroid = count_centroid(c_x, c_y, c_z)
            continue

    invalid_cluster_elements = cluster[indices_to_remove]
    cluster = np.delete(cluster, indices_to_remove, axis=0)

    return cluster, invalid_cluster_elements, new_centroid

def check_elements_corr_to_centroid(cluster, invalid_cluster_values, centroid, corr_to_check, non_corr_elements):
    this_cluster = np.copy(cluster)
    indicies = []
    centroid = np.array(centroid)

    for i in range(len(invalid_cluster_values)):
        corr = np.corrcoef(invalid_cluster_values[i], centroid)[0][1]
        if(corr > corr_to_check):
            indicies.append(i)
            this_cluster = np.append(this_cluster, np.array([invalid_cluster_values[i]]), axis=0)

    if len(indicies) == 0:
        if len(invalid_cluster_values) > 0:
            indicies.append(0)
            non_corr_elements.append(invalid_cluster_values[0])

    invalid_cluster_values = np.delete(invalid_cluster_values, indicies, axis=0)
    return this_cluster, invalid_cluster_values, centroid