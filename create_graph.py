"""
A script that contains functions extracting the cluster medoid from a .csv file
"""
from sklearn.cluster import KMeans
from sklearn import metrics
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

def extract_medoids(file_path):
    """
    Extracts the data from a given csv file, calculates and returns the medoids
    :param file_path: the location of the file to extract
    :return: medoids with their coordinates
    """

    locations = pd.read_csv(file_path)
    print(locations)
    x = locations['x']
    y = locations['y']
    

    plt.plot()
    X = np.array(list(zip(x, y))).reshape(len(x), 2)
    colors = ['b', 'g', 'c']
    markers = ['o', 'v', 's']

    # KMeans algorithm 
    K = 3
    kmeans_model = KMeans(n_clusters=K).fit(X)

    print(kmeans_model.cluster_centers_)
    centers = np.array(kmeans_model.cluster_centers_)

    plt.plot()
    plt.title('k means centroids')

    for i, l in enumerate(kmeans_model.labels_):
        plt.plot(x[i], y[i], color=colors[l], marker=markers[l],ls='None')

    plt.scatter(centers[:,0], centers[:,1], marker="x", color='r')
    plt.show()

if __name__ == '__main__':
    file_name = "cluster_assignments/brca/TCGA-LL-A442-01Z-00-DX1_clusters.csv"
    path = 'cluster_assignments/brca/'
    extract_medoids(file_path=file_name)
