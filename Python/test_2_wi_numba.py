# Initialization of big array
# Author:  Magic Yang
# Version: 1.0
# Date:    2020.09.18
# with numba acceleration

import time
import numpy as np
from numba import vectorize, int64

num_loops = 50
img1 = np.ones((1000,1000), np.int64) * 5
img2 = np.ones((1000,1000), np.int64) * 10
img3 = np.ones((1000,1000), np.int64) * 15

def add_arrays(img1, img2, img3):
    return np.square(img1+img2+img3)

start1 = time.time()

for i in range(num_loops):
    result = add_arrays(img1, img2, img3)

end1 = time.time()

run_time1 = end1 - start1

print('Average time for normal numpy operation={}'.format(run_time1/num_loops))

@vectorize([int64(int64,int64,int64)], target='parallel') # target = cpu/parallel/cuda

def add_arrays_numba(img1, img2, img3):
    return np.square(img1+img2+img3)

start2 = time.time()

for i in range(num_loops):
    result = add_arrays_numba(img1, img2, img3)

end2 = time.time()

run_time2 = end2 - start2

print('Average time using numba accelerating={}'.format(run_time2/num_loops))