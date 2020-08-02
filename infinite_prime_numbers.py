#! /usr/bin/env python3

import time
from math import sqrt

start = time.time()

period = 10

current = 2
print(current)
while True:
    current += 1
    if current % 2 == 1:
        for i in range(2, int(sqrt(current))):
            if current % i == 0: 
                break
        else:
            print(current)
    if time.time() > start + period:
        break