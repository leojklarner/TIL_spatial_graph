from utilities import get_file_locations
import os.path

output_file_path = "metrics_output.csv"

# getting the file locations
locations = get_file_locations('metadata.csv', 'cluster_assignments')

# creating an output file to which to append the results
if not os.path.isfile(output_file_path):
    with open(output_file_path,'w') as output:
        output.write('slide_name,average_clustering_coefficient,average_degree,average_closeness_centrality, '
                     'average_betweenness_centrality,average_eccentricity}')
        output.close()
