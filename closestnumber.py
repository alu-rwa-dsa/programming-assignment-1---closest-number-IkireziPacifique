#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the closestNumbers function below.
def closestNumbers(arr):
    # Sorting the array
    arr.sort()
    diff = []
    prev = 0
    # Calculating the difference
    for i in range(1, len(arr)):
        # Finding if there is no duplicate
        if arr[prev] == arr[i]:
            return "Not unique"
        # Making difference of each pair
        diff.append(arr[i] - arr[prev])
        prev = prev + 1
        
    minf = min(diff)
    prev = 0 
    newarr = []
    for i in range(1, len(arr)):
        # Finding the pair with the min difference 
        if arr[i] - arr[prev] == minf:
            newarr.append(arr[prev])
            newarr.append(arr[i])
        prev = prev + 1
    return newarr

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    result = closestNumbers(arr)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
