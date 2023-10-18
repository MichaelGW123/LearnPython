import numpy as np


def compare_arrays(array1, array2):
    are_equal = np.all(array1 == array2)

    if are_equal:
        print('The arrays are equal.')
    else:
        print('The arrays are not equal.')
        print('Diff: ', np.subtract(array1, array2))


# Example data (replace these with your actual arrays)
array1 = np.array([1, 2, 3, 4, 5])
array2 = np.array([1, 2, 2, 4, 5])

# Compare arrays
compare_arrays(array1, array2)
