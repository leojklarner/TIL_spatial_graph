"""
This script contains all the functionalities needed to calculate
the desired graph metrics and save them to a .csv file
"""

import networkx as nx


def calculate_metrics(slide_name, graph, output_file):
    """
    Takes a graph object, calculates the desired metrics and writes them to a file.
    :param graph: a NetworkX graph object representing clusters of TIL cells
    :param slide_name: the name of the slide represented by the graph
    :param output_file: the location of the file to which the measures should be written
    :return: write the respective metrics to a file
    """

    # calculate the average clustering coefficient
    average_clustering_coefficient = nx.algorithms.average_clustering(graph, weight='weight')

    # calculate the average degree
    average_degree = 0
    for node, degree in graph.degree(weight='weight'):
        average_degree = average_degree + degree
    average_degree = average_degree/len(graph.degree)

    # calculate the average closeness centrality
    average_closeness_centrality = 0
    closeness_centralities = nx.algorithms.centrality.closeness_centrality(graph, distance='weight')
    for node, closeness in closeness_centralities.items():
        average_closeness_centrality = average_closeness_centrality + closeness
    average_closeness_centrality = average_closeness_centrality/len(closeness_centralities)

    # calculate the average betweenness centrality
    average_betweenness_centrality = 0
    betweenness_centralities = nx.algorithms.centrality.betweenness_centrality(graph, weight='weight')
    for node, betweenness in betweenness_centralities.items():
        average_betweenness_centrality = average_betweenness_centrality + betweenness
    average_betweenness_centrality = average_betweenness_centrality/len(betweenness_centralities)


    # calculate the average shortest path distance
    average_shortest_path = nx.algorithms.shortest_paths.average_shortest_path_length(graph, weight='weight')

    with open(output_file, 'a') as output:
        output.write(f'{slide_name},{average_clustering_coefficient},{average_degree},'
                     f'{average_closeness_centrality},{average_betweenness_centrality},'
                     f'{average_shortest_path}\n')


if __name__ == '__main__':
    G = nx.Graph()
    G.add_edge(1, 2)
    G.add_edge(1, 3)
    G.add_edge(1, 5)
    G.add_edge(2, 3)
    G.add_edge(3, 4)
    G.add_edge(4, 5)
    calculate_metrics("hello", G, "metrics_output.csv")
