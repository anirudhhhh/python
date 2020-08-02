#! /usr/bin/env python3
import time

num1 = 0
num2 = 1

while True:
    print(num2)
    print

    num3 = num1 + num2
    num1 = num2
    num2 = num3
    time.sleep(1/2)