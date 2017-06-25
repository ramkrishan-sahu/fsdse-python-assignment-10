import numpy as np
def convert(array):
    cel_array = []
    for i in array:
        f_c = (i * 1.8) +32
        cel_array = np.append(cel_array, f_c)
    return cel_array
