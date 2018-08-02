# coding: utf-8

import multiprocessing as mp
import random
import string


def rand_string(length, output):
    rand_str = ''.join(random.choice(string.ascii_lowercase + string.ascii_uppercase)
                       for i in range(length))
    output.put(rand_str)


output = mp.Queue()

processes = [mp.Process(target=rand_string, args=(5, output))
             for x in range(4)]

for p in processes:
    p.start()
for p in processes:
    p.join()

results = [output.get() for p in processes]
print(results)
