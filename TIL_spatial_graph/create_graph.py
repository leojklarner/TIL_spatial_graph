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
    print(loc_df)

    grouped = loc_df.sort_values(by= 'cluster_id')
    unique_id = loc_df['cluster_id'].unique().tolist()

    i = 0
    pos = {}
    for cluster in unique_id:
        v = loc_df[loc_df.cluster_id == cluster]
        print('V = \n', v)
        x = v.x.to_numpy().mean()
        y = v.y.to_numpy().mean()

        pos.update({i:(x,y)})
        i += 1


    # Generate a network
    G = nx.Graph()
    G.add_nodes_from(pos.keys())
    for n,p in pos.items():
        G.nodes[n]['pos'] = p

    print(nx.get_node_attributes(G,'check'))
    #nx.draw(G,pos)
    #plt.show()

    return G


if __name__ == '__main__':
    file_name = "TIL_spatial_graph/cluster_assignments/brca/TCGA-LL-A442-01Z-00-DX1_clusters.csv"
    path = 'cluster_assignments/brca/'
    extract_centroids(file_path=file_name)