"""
A script that contains functions extracting the cluster medoid from a .csv file
"""

import pandas as pd

def extract_medoids(file_path):
    """
    Extracts the data from a given csv file, calculates and returns the medoids
    :param file_path: the location of the file to extract
    :return: medoids with their coordinates
    """

    locations = pd.read_csv(file_path)
    print(locations)

if __name__ == '__main__':
    file_name = "cluster_assignments/brca/TCGA-LL-A442-01Z-00-DX1_clusters.csv"
    path = 'cluster_assignments/brca/'
    extract_medoids(file_path=file_name)