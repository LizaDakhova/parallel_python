# coding: utf-8

import multiprocessing as mp
import math
import time
import argparse


def sqrt_of_module(x):
    return math.sqrt(abs(x))


def to_print(interval, output):
    if interval != 'none' and interval != 'None':
        start, end = interval.split(':')
        print(output[int(start) : int(end)])


# parse args
parser = argparse.ArgumentParser()
parser.add_argument('-n', help='number in range function')
parser.add_argument('-cores', help='number of cores', default='4')
parser.add_argument('-interval', help='interval to print; \n examples: "none", "None", "1:5"', default='None')
p = parser.parse_args()
n = int(p.n)
interval = p.interval
cores = int(p.cores)


# with using usual multiprocessing
print("--- using usual multiprocessing ---")
start_time = time.time()
pool = mp.Pool(processes=cores)
output1 = pool.map(sqrt_of_module, range(n))
to_print(interval, output1)
print("--- lasts %s seconds ---\n" % (time.time() - start_time))


# with map async
print("--- using async multiprocessing ---")
start_time = time.time()
pool = mp.Pool(processes=cores)
results = pool.map_async(sqrt_of_module, range(n))
output2 = results.get()
to_print(interval, output2)
print("--- lasts %s seconds ---\n" % (time.time() - start_time))


# without using multiprocessing
print("--- without using multiprocessing ---")
start_time = time.time()
output3 = list(map(sqrt_of_module, range(n)))
to_print(interval, output3)
print("--- lasts %s seconds ---\n" % (time.time() - start_time))
