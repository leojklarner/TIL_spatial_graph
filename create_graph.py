"""
A script that contains functions extracting the cluster medoid from a .csv file
"""

import pandas as pd
import sklearn as sk
import numpy as np
import networkx as nx
import matplotlib.pyplot as plt



def extract_centroids(file_path):
    """
    Extracts the data from a given csv file, calculates the centroids and builds a graph
    :param file_path: the location of the file to extract
    :return: medoids with their coordinates
    """
    # Calculate the centroids 
    loc_df = pd.read_csv(file_path)

    grouped = loc_df.sort_values(by= 'cluster_id')
    unique_id = loc_df['cluster_id'].unique().tolist()

    i = 0
    pos = {}
    posArray = np.zeros((len(unique_id),2))
    dists = np.empty((len(unique_id) - 1,len(unique_id) - 1))
    dists[:] = np.NaN
    for cluster in unique_id:
        v = loc_df[loc_df.cluster_id == cluster]
        x = v.x.to_numpy().mean()
        y = v.y.to_numpy().mean()

        posArray[i,:] = x,y
        pos.update({i:(x,y)})
        i += 1

    # Distances between nodes
    for j in range(length(unique_id)):

        for 
        dxdy = posArray[j,:] - posArray[j+i,:]





    # Generate a network
        # Nodes
    G = nx.Graph()
    G.add_nodes_from(pos.keys())
    for n,p in pos.items():
        G.nodes[n]['pos'] = p

        # Egdes
    j = listpos.values()
    print(j)

    #for point in j:
    #    sk.metrics.euclidean_distances()
#
    #print(nx.get_node_attributes(G,'check'))
    ##nx.draw(G,pos)
    ##plt.show()

    return G


if __name__ == '__main__':
    file_name = "cluster_assignments/brca/TCGA-LL-A442-01Z-00-DX1_clusters.csv"
    path = 'cluster_assignments/brca/'
    extract_centroids(file_path=file_name)