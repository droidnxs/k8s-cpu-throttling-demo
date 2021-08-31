#!/usr/bin/env python
import time

def recursiveFib(n):
    if n == 1 or n == 2:
        return 1

    return recursiveFib(n - 1) + recursiveFib(n - 2)


if __name__ == '__main__':
    while True:
        start = time.perf_counter()
        recursiveFib(35)
        end = time.perf_counter()
        print(f"Took {end - start:0.4f} seconds")