"""
This script contains all the functionalities needed to calculate
the desired graph metrics and save them to a .csv file
"""

import networkx as nx
from networkx.algorithms.centrality import degree_centrality
import matplotlib.pyplot as plt


def calculate_metrics(slide_name, graph, output_file):
    """
    Takes a graph object, calculates the desired metrics and writes them to a file.
    :param graph: a NetworkX graph object representing clusters of TIL cells
    :param slide_name: the name of the slide represented by the graph
    :param output_file: the location of the file to which the measures should be written
    :return: write the respective metrics to a file
    """

    print(f'Calculating metrics for {slide_name}')

    # calculate the average clustering coefficient
    average_clustering_coefficient = nx.algorithms.average_clustering(graph)

    # calculate the average degree
    average_degree = 0
    for node, degree in graph.degree:
        average_degree = average_degree + degree
    average_degree = average_degree/len(graph.degree)

    # calculate the average closeness centrality
    average_closeness_centrality = 0
    closeness_centralities = nx.algorithms.centrality.closeness_centrality(graph)
    for node, closeness in closeness_centralities.items():
        average_closeness_centrality = average_closeness_centrality + closeness
    average_closeness_centrality = average_closeness_centrality/len(closeness_centralities)

    # calculate the average betweenness centrality
    average_betweenness_centrality = 0
    betweenness_centralities = nx.algorithms.centrality.closeness_centrality(graph)
    for node, betweenness in betweenness_centralities.items():
        average_betweenness_centrality = average_betweenness_centrality + betweenness
    average_betweenness_centrality = average_betweenness_centrality/len(betweenness_centralities)

    # calculate the average eccentricity
    average_eccentricity = 0
    eccentricities = nx.algorithms.distance_measures.eccentricity(graph)
    for node, eccentricity in eccentricities.items():
        average_eccentricity = average_eccentricity + eccentricity
    average_eccentricity = average_eccentricity/len(eccentricities)

    with open(output_file, 'a') as output:
        output.write(f'{slide_name},{average_clustering_coefficient},{average_degree},'
                     f'{average_closeness_centrality},{average_betweenness_centrality},'
                     f'{average_eccentricity}\n')

    print(f'Metrics calculated for {slide_name}')


if __name__ == '__main__':
    G = nx.Graph()
    G.add_edge(1, 2)
    G.add_edge(1, 3)
    G.add_edge(1, 5)
    G.add_edge(2, 3)
    G.add_edge(3, 4)
    G.add_edge(4, 5)
    calculate_metrics("hello", G, "metrics_output.csv")
