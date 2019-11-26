


#!/bin/python3

import math
import os
import random
import re
import sys
from typing import List 

# Complete the arrayManipulation function below.
def arrayManipulation(n: int, queries: List[int]) -> int:
    max_val: int = 0

    # (1) init array of zeroes 
    b_arr: list = n * [0]
    
    # loop to  update array and max_val
    for _,q in enumerate(queries):
        for i,e in enumerate(b_arr[q[0]-1:q[1]]):
            
            # (2) perform operations
            b_arr[q[0]+i-1] += q[2]
    
            # (3) update max_val
            if b_arr[q[0]-1+i] > max_val:
                max_val = b_arr[q[0]-1+i]
            
        # print('b_arr {0}:\t'.format(_), b_arr)
    
    # print('b_arr_final:\t', b_arr)
    return max_val

    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    nm = input().split()
    n = int(nm[0])
    m = int(nm[1])

    queries = []

    for _ in range(m):
        queries.append(list(map(int, input().rstrip().split())))

    result = arrayManipulation(n, queries)
    fptr.write(str(result) + '\n')
    fptr.close()
