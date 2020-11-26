"""
A script that contains functions extracting the cluster centroid from a .csv file
"""

import pandas as pd
import sklearn as sk
import numpy as np
import networkx as nx
import matplotlib.pyplot as plt
import itertools
from scipy.spatial.distance import euclidean


def centroids_to_graph(file_path):
    """
    Extracts the data from a given csv file, calculates the centroids and builds a graph
    :param file_path: the location of the file to extract
    :return: centroids with their coordinates
    """

    # extract centroid data
    location_data = pd.read_csv(file_path)
    centroids = location_data.groupby(by=["cluster_id"]).mean()

    cluster_id = centroids.index.tolist()
    coordinates = np.column_stack([centroids['x'].values, centroids['y'].values])

    # create graph and add nodes
    G = nx.Graph()
    G.add_nodes_from(cluster_id)

    # add edges
    for idx1 in range(0, len(cluster_id)):
        for idx2 in range(idx1+1, len(cluster_id)):
            distance = euclidean(coordinates[idx1], coordinates[idx2])
            G.add_edge(cluster_id[idx1], cluster_id[idx2], weight=distance)

    return G

if __name__ == '__main__':
    file_name = "cluster_assignments/brca/TCGA-3C-AALI-01Z-00-DX1_clusters.csv"
    centroids_to_graph(file_path=file_name)
