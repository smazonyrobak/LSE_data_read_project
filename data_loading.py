import h5py
import numpy as np

def load_sleap_file(analysisfile=None):
    if analysisfile is None:
        print("\033[93mNo File path provided, loading default data.\033[0m")
        analysisfile = "./first_sample_analysis.h5"

    with h5py.File(analysisfile, 'r') as af:
        dataset = np.array(af["tracks"][:].T)  # loads and transposes core tracking data. Dataset has four dimensions: frames, nodes, coordinates and instances (num. of animals)exi
        dataset_keys = list(af.keys())  # create a list containing dataset keys
        tracked_bodypart_names = np.array([n.decode() for n in af['node_names'][
                                                               :]])  # loads names of body parts of mice that are tracked and converts them from binary

    return dataset, dataset_keys, tracked_bodypart_names


