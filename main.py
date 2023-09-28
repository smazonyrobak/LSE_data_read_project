import h5py
import numpy as np

file_found = False  # Flag to indicate if the file is found or not
analysisfile = None
try:
    analysisfile = 'path/to/file'
    with h5py.File(analysisfile, 'r'):
        file_found = True  # Set the flag to True because the file was found
except FileNotFoundError:
    print("\033[93mFile not found in the specific directory. Trying the current directory.\033[0m")

if not file_found:
    try:
        analysisfile = "first_sample_analysis.h5"
        print("\033[94mtried to find a file: ", str(analysisfile), "\033[0m")
        with h5py.File(analysisfile, 'r'):
            file_found = True  # Sets the flag to True because the file has been found
    except FileNotFoundError:
        print("\033[91mFile not found in both specified nor own directory. Exiting.\033[0m")
        exit()

with h5py.File(analysisfile, 'r') as af:
    dataset = np.array(af["tracks"][:].T) #loads and transposes core tracking data. Dataset has four dimensions: frames, nodes, coordinates and instances (num. of animals)
    dataset_keys = list(af.keys()) #create a list containing dataset keys
    tracked_bodypart_names = np.array([n.decode() for n in af['node_names'][:]]) #loads names of body parts of mice that are tracked and converts them from binary

while True:
    what_to_do = str(input("\n Do you want to: \n a) visualise the data structure - write s \n"
                           " b) visualize mice tracking - write t \n"
                           "c) interpolate the data - write i \n"
                           "d) exit the program - write e)"))

    #from here on, depending on the desired actions, other executables are called
    if what_to_do == "s":
        with open("datastructure_read.py") as dr:
            exec(dr.read())
    elif what_to_do == "t":
        with open("micetracker.py") as mt:
            exec(mt.read())
    elif what_to_do == "i":
        with open ("missing_values_interpolater.py") as mvi:
            exec(mvi.read())
    elif what_to_do == "e":
        exit()
    else:
        print("Invalid option, please try again")