from utilities import get_file_locations
from calculate_statistics import calculate_metrics
from create_graph import centroids_to_graph
import os.path
import time

output_file_path = "metrics_output.csv"

start_time = time.time()

# getting the file locations
locations = get_file_locations('metadata.csv', 'cluster_assignments')

# creating an output file to which to append the results
if not os.path.isfile(output_file_path):
    with open(output_file_path,'w') as output:
        output.write('slide_name,average_clustering_coefficient,average_degree,average_closeness_centrality, '
                     'average_betweenness_centrality,average_eccentricity}')
        output.close()

for name, path in locations.items():
    subroutine_start = time.time()
    print(f'Starting routine for {path}')

    slide_graph = centroids_to_graph(path)

    subroutine_middle = time.time()
    print(f'Calculated graph for {path} in {subroutine_middle-subroutine_start}')

    calculate_metrics(slide_name=name, graph=slide_graph, output_file=output_file_path)

    subroutine_end = time.time()
    print(f'Calculated metrics for {path} in {subroutine_end-subroutine_middle}')

end_time = time.time()
print(f'The programme finished in {end_time-start_time}.')
