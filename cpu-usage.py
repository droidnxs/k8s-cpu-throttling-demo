#!/usr/bin/env python
"""
Produces load on all available CPU cores
Updated with suggestion to prevent Zombie processes
Linted for Python 3
Source: 
insaner @ https://danielflannery.ie/simulate-cpu-load-with-python/#comment-34130
"""

if __name__ == '__main__':
    x = 2
    for i in range(0, 1000000000):
        x = x * x