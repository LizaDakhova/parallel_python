# coding: utf-8

import multiprocessing as mp
import math
import time
import argparse

# parse args
parser = argparse.ArgumentParser()
parser.add_argument('-n', help='number in range function')
parser.add_argument('-cores', help='number of cores', default='4')
p = parser.parse_args()
n = int(p.n)
cores = int(p.cores)


def sqrt_of_module(x):
    return math.sqrt(abs(x))


# with using multiprocessing
start_time = time.time()
pool = mp.Pool(processes=cores)
results = pool.map(sqrt_of_module, range(n))
# print(results)
print("--- using multiprocessing it lasts %s seconds ---" % (time.time() - start_time))


# without using multiprocessing
start_time = time.time()
results = map(sqrt_of_module, range(n))
# print(list(results)[-5:])
print("--- without using multiprocessing it lasts %s seconds ---" % (time.time() - start_time))
