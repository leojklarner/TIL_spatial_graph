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
    betweenness_centralities = nx.algorithms.centrality.current_flow_betweenness_centrality(graph, weight='weight')
    for node, betweenness in betweenness_centralities.items():
        average_betweenness_centrality = average_betweenness_centrality + betweenness
    average_betweenness_centrality = average_betweenness_centrality/len(betweenness_centralities)

    # calculate the average shortest path distance
    average_shortest_path = nx.algorithms.shortest_paths.average_shortest_path_length(graph, weight='weight')

    # calculate the size of the maximum weight clique
    clique, weight_clq = nx.algorithms.clique.max_weight_clique(graph, weight='weight')
    max_clique_num = len(clique)
    max_clique_weight = weight_clq

    # calculate average neighbour degree
    average_neighbour_degree = 0
    node_avg = nx.algorithms.assortativity.average_neighbor_degree(graph, weight='weight')
    for node, avg in node_avg.items():
        average_neighbour_degree = average_neighbour_degree + avg
    average_neighbour_degree = average_neighbour_degree/len(node_avg)

    # calculate average degree connectivity
    average_degree_connectivity = 0
    conn_avg = nx.algorithms.assortativity.average_degree_connectivity(graph, weight='weight')
    for node, avg in conn_avg.items():
        average_degree_connectivity = average_degree_connectivity + avg
    average_degree_connectivity = average_degree_connectivity/len(node_avg)

    # calculate the average eigenvector centrality
    average_eigenvector_centrality = 0
    eigenvector_centrality = nx.algorithms.centrality.eigenvector_centrality(graph, weight='weight')
    for node, eigenvector in eigenvector_centrality.items():
        average_eigenvector_centrality = average_eigenvector_centrality + eigenvector
    average_eigenvector_centrality = average_eigenvector_centrality/len(betweenness_centralities)

    # calculate the average load centrality
    average_load_centrality = 0
    load_centrality = nx.algorithms.centrality.load_centrality(graph, weight='weight')
    for node, load in load_centrality.items():
        average_load_centrality = average_load_centrality + load
    average_load_centrality = average_load_centrality/len(load_centrality)

    # calculate the average harmonic centrality
    average_harmonic_centrality = 0
    harmonic_centrality = nx.algorithms.centrality.harmonic_centrality(graph, distance='weight')
    for node, harmonic in harmonic_centrality.items():
        average_harmonic_centrality = average_harmonic_centrality + harmonic
    average_harmonic_centrality = average_harmonic_centrality/len(harmonic_centrality)

    # calculate the average current_flow_closeness_centrality centrality
    average_current_flow_closeness_centrality = 0
    current_flow_centrality = nx.algorithms.centrality.current_flow_closeness_centrality(graph, weight='weight')
    for node, flow in current_flow_centrality.items():
        average_current_flow_closeness_centrality = average_current_flow_closeness_centrality + flow
    average_current_flow_closeness_centrality = average_current_flow_closeness_centrality/len(current_flow_centrality)

    with open(output_file, 'a') as output:
        output.write(f'{slide_name},{average_clustering_coefficient},{average_degree},'
                     f'{average_closeness_centrality},{average_betweenness_centrality},'
                     f'{average_shortest_path},{max_clique_num},{max_clique_weight},'
                     f'{average_neighbour_degree},{average_degree_connectivity},'
                     f'{average_eigenvector_centrality},{average_load_centrality},'
                     f'{average_harmonic_centrality},{average_current_flow_closeness_centrality}\n')


if __name__ == '__main__':
    G = nx.Graph()
    G.add_edge(1, 2, weight=2)
    G.add_edge(1, 3, weight=3)
    G.add_edge(1, 5, weight=4)
    G.add_edge(2, 3, weight=5)
    G.add_edge(3, 4, weight=6)
    G.add_edge(4, 5, weight=7)
    calculate_metrics("hello", G, "metrics_output.csv")
