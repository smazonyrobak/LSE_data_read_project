print("===analysisfile===")
print(analysisfile)
print()

print("\033[92m======list of the whole dataset======\033[0m")
print(dataset)
print("\033[92mshape:\033[0m", dataset.shape)
print()

print("\033[92m======list of all of the dataset keys======\033[0m")
print(dataset_keys)
print()

print("\033[92m======list of tracked body parts======\033[0m")
print(tracked_bodypart_names)
print("\033[92mshape:\033[0m", tracked_bodypart_names.shape)
print()

frames, bodypart_count, coordinates, animal_number = dataset.shape
print("\033[92mshape of number of frames:\033[0m", frames)
print("\033[92mshape of number of body parts:\033[0m", bodypart_count)
print("\033[92mshape of coordinates:\033[0m", coordinates)
print("\033[92mshape of animals' count:\033[0m", animal_number)
print()

print("\033[92m==MISSING VALUES==\033[0m")

for bp, ds in zip(tracked_bodypart_names, range(dataset.shape[1])):
    sum_missing_val_data = np.sum(np.isnan(dataset[:, ds, 0, 0]))
    print(bp,":", sum_missing_val_data) #prints all missing values for all body parts


