"""
A script containing various utilities.
"""

import pandas as pd
import os
import re


def get_file_locations(path_to_metadata, data_directory):
    """
    This function extracts the file paths to all csv file for which
    metadata is available nad returns them as a dict
    :param path_to_metadata: the location of the metadata file
    :param data_directory: the directory containing the data csv files
    :return: a dict with the names of the slides as keys and the
             directories as arguments
    """

    # get a list with the IDs of the slides that have metadata
    slides_with_metadata = pd.read_csv(path_to_metadata, usecols=["SlideID"])["SlideID"].to_list()

    # extract the file paths of all the slide IDs in the above list
    slide_paths = {}
    id_stem = re.compile("(.*?)_clusters.csv")
    for cancer_type in os.listdir(data_directory):
        for slide in os.listdir(data_directory+'/'+cancer_type):
            file_id = re.findall(id_stem, slide)[0]
            if file_id in slides_with_metadata:
                slide_paths[file_id] = data_directory+'/'+cancer_type+'/'+slide

    return slide_paths
