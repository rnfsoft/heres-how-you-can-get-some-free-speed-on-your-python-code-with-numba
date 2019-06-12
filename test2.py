# Numpy testing
import time

from numba import vectorize, int64
import numpy as np

num_loops = 50
img_1 = np.ones((1000,1000), np.int64) * 5
img_2 = np.ones((1000,1000), np.int64) * 10
img_3 = np.ones((1000,1000), np.int64) * 15

@vectorize([int64(int64, int64, int64)], target="parallel")
def add_arrays(img_1, img_2, img_3):
    return np.square(img_1 + img_2 + img_3)

start = time.time()

for i in range(num_loops):
    result = add_arrays(img_1, img_2, img_3)

end = time.time()

run_time = end - start

print("Average time = {}".format(run_time/num_loops))

