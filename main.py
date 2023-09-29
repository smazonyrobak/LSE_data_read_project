from data_loading import load_sleap_file
from datastructure_read import datastructure_read
from missing_values_interpolater import point_finder, point_finder_simple
from micetracker import micetrack

analysisfile="./first_sample_analysis.h5"
dataset, dataset_keys, tracked_bodypart_names = load_sleap_file()

while True:
    what_to_do = str(input("\n Do you want to: \n a) visualise the data structure - write a \n"
                           " b) visualize mice tracking - write b \n"
                           "c) see data about missing values for head - write c \n"
                           "d) exit the program - write d)"))

    #from here on, depending on the desired actions, other functions from other files are called
    if what_to_do == "a":
        datastructure_read(analysisfile, dataset, dataset_keys, tracked_bodypart_names) #prints data structure info
    elif what_to_do == "b": #prints tracking of mice
         micetrack()
    elif what_to_do == "c": #prints head missing values info
        print("\033[92mnumber of individual periods with no values assigned for head (using while loop):\033[0m\n", len(point_finder(dataset)))
        print("\033[92m2D array of respectively first and last value between NaN blocks in head body part (using while loop):\033[0m\n", point_finder(dataset))
        pairs = point_finder(dataset)
        number = 0
        for x in pairs:
            number += ((x[1]-1) - x[0]) #I am subtracting 1 from x[1] because e.g. [T, F, F ,F ,T] has 3 F's but would otherwise be counted as 4 F's
        print("\033[92mcount of numbers in the interval (using while loop):\033[0m\n", number)

        print("\033[92mtransition indices for video frames using np.isnan (changes of T -> F or F -> T):\033[0m\n", point_finder_simple(dataset))
        print("\033[92mcount of transition points (changes of T -> F or F -> T):\n\033[0m", len(point_finder_simple(dataset)))

    elif what_to_do == "d": #exits program
        exit()
    else:
        print("Invalid option, please try again")