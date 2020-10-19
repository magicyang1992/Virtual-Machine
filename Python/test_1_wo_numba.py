# Test insertion sort with and w/o numba
# Author:  Magic Yang
# Version: 1.0
# Date:    2020.09.17
# w/o numba acceleration

import time
import random

num_loops = 50
len_of_list = 100000

def insertion_sort(arr):
    for i in range(len(arr)):
        cursor = arr[i]
        pos = i

        while pos > 0 and arr[pos-1] > cursor:
            arr[pos] = arr[pos-1]
            pos = pos - 1
        arr[pos] = cursor
    return arr

start = time.time()
list_of_numbers = list()
for i in range(len_of_list):
    num = random.randint(0, len_of_list)
    list_of_numbers.append(num)

for i in range(num_loops):
    result = insertion_sort(list_of_numbers)

end = time.time()

run_time = end - start
print('Average time = {}'.format(run_time/num_loops))