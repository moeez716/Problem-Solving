
#!/bin/python3
#Problem Solving
#Given an array of integers, calculate the ratios of its elements that are , , and . Print the decimal value of each fraction on a new line with 6 places after the decimal.
#input
# arr = [-4, 3, -9, 0, 4, 1]
#output
# 0.500000
# 0.333333
# 0.166667

import math
import os
import random
import re
import sys

#
# Complete the 'plusMinus' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def plusMinus(arr):
    n=len(arr)
    pos=0
    neg=0
    zero=0
    for i in range(0,n):
        if arr[i]<0:
            neg=neg+1
        elif arr[i]>0:
            pos=pos+1
        elif arr[i]==0:
            zero=zero+1
    print(round(pos/n,6))
    print(round(neg/n,6))
    print(round(zero/n,6))        
                






if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
