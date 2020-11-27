from utilities import get_file_locations
from calculate_statistics import calculate_metrics
from create_graph import centroids_to_graph
import os.path
import time

output_file_path = "metrics_output_additional.csv"

start_time = time.time()

# getting the file locations
locations = get_file_locations('metadata.csv', 'cluster_assignments')

# creating an output file to which to append the results
if not os.path.isfile(output_file_path):
    with open(output_file_path,'w') as output:
        output.write('slide_name,average_clustering_coefficient},average_degree,'
                     'average_closeness_centrality,average_betweenness_centrality,'
                     'average_shortest_path,max_clique_num,max_clique_weight,'
                     'average_neighbour_degree,average_degree_connectivity,'
                     'average_eigenvector_centrality,average_load_centrality,'
                     'average_harmonic_centrality,average_current_flow_closeness_centrality\n')
        output.close()

# run convert the location data to a graph and run the analysis
for name, path in list(locations.items()):
    subroutine_start = time.time()

    slide_graph = centroids_to_graph(path)
    calculate_metrics(slide_name=name, graph=slide_graph, output_file=output_file_path)

    subroutine_end = time.time()
    print(f'Finished for {path} in {subroutine_end-subroutine_start}')

end_time = time.time()
print(f'The programme finished in {end_time-start_time}.')
