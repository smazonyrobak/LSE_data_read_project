print("===analysisfile===")
print(analysisfile)
print()

print("\033[92m======list of the whole dataset======\033[0m")
print(dataset)
print("\033[93mshape:\033[0m", dataset.shape)
print()

print("\033[92m======list of all of the dataset keys======\033[0m")
print(dataset_keys)
print()

print("\033[92m======list of tracked body parts======\033[0m")
print(tracked_bodypart_names)
print("\033[93mshape:\033[0m", tracked_bodypart_names.shape)
print()

frames, bodypart_count, coordinates, animal_number = dataset.shape
print("\033[93mshape of number of frames:\033[0m", frames)
print("\033[93mshape of number of body parts:\033[0m", bodypart_count)
print("\033[93mshape of coordinates:\033[0m", coordinates)
print("\033[93mshape of animals' count:\033[0m", animal_number)
print()