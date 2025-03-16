#!/bin/python3
#Given a square matrix, calculate the absolute difference between the sums of its diagonals.

#For example, the square matrix  is shown below:

# 1 2 3
# 4 5 6
# 9 8 9  
# The left-to-right diagonal =1+2+9 .
# The right-to-left diagonal =3+5+9 .
# Their absolute difference is |15-17|=2
import math
import os
import random
import re
import sys

#
# Complete the 'diagonalDifference' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY arr as parameter.
#

def diagonalDifference(arr):
    n=len(arr)
    leftsum=0
    rightsum=0
    for i in range(0,n):
        leftsum=arr[i][n-1-i]+leftsum
        rightsum=rightsum+arr[i][i]
    if leftsum-rightsum<0:
        return -(leftsum-rightsum)
    elif leftsum-rightsum>0:
        return leftsum-rightsum
    else:
        return 0   
    
                
            
   

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    result = diagonalDifference(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
