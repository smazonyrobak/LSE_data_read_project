def linear_interpolation(array):
    missing_values = np.where(~np.isnan(array))[0]
    if len(missing_values) < 2:
        return array
    else:
        last_valid_value = None
        for value in array:
            if not np.isnan(value):
                if last_valid_value is not None:
                    print(last_valid_value, value)
                last_valid_value = value
            elif last_valid_value is not None:
                continue

linear_interpolation(dataset[:, 0, 0, 0])







