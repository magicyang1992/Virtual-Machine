# Initialization of big array
# Author:  Magic Yang
# Version: 1.0
# Date:    2020.09.18
# w/o numba acceleration

import time
import numpy as np

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

