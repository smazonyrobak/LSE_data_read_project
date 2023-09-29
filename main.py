import h5py

from data_loading import load_sleap_file
from datastructure_read import datastructure_read


fpath="./first_sample_analysis.h5"
dataset, dataset_keys, tracked_bodypart_names = load_sleap_file()

while True:
    what_to_do = str(input("\n Do you want to: \n a) visualise the data structure - write s \n"
                           " b) visualize mice tracking - write t \n"
                           "c) interpolate the data - write i \n"
                           "d) exit the program - write e)"))

    #from here on, depending on the desired actions, other executables are called
    if what_to_do == "s":
        datastructure_read(fpath, dataset, dataset_keys, tracked_bodypart_names)
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