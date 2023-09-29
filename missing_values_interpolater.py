import numpy as np

def point_finder(array):
    pairs = []
    i = 1
    while i < array.shape[0]:
        value_1 = array[i, 0, 0, 0]
        value_1_before = array[i-1, 0, 0, 0]
        if np.isnan(value_1) and not np.isnan(value_1_before):
            for ii in range(i+1, array.shape[0]):
                value_2 = array[ii, 0, 0, 0]
                value_2_before = array[ii-1, 0, 0, 0]
                if not np.isnan(value_2) and np.isnan(value_2_before):
                    pairs.append ([i-1, ii])
                    i = ii + 1
                    break
        else:
            i += 1
    return(pairs)


def point_finder_simple(array):
    Nan_list = np.isnan(array[:, 0, 0, 0])
    Nan_list_change = np.logical_xor(Nan_list != np.roll(Nan_list, 1), Nan_list != np.roll(Nan_list, -1))
    indices_where_true = np.where(Nan_list_change)[0]  # This will give you the indices where Nan_list_change is True
    return list(indices_where_true)

