#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'gridChallenge' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING_ARRAY grid as parameter.
#

def gridChallenge(grid):

    sorted_rows = [''.join(sorted(row)) for row in grid]
    
    for col in range(len(sorted_rows[0])):
        for row in range(1, len(sorted_rows)):
            if sorted_rows[row][col] < sorted_rows[row - 1][col]:
                return "NO"
    return "YES"
def test_gridChallenge():
    test_cases = [
        (['abc', 'bcd', 'cde'], "YES"),  
        (['dab', 'bac', 'cab'], "NO"),   
        (['zab', 'yba', 'xyx'], "NO"),   
        (['a'], "YES"),                            
        (['abcd'], "YES"),              
        (['a', 'b', 'a'], "NO"),       
        (['a', 'b', 'c'], "YES"),        
        (['ebacd', 'fghij', 'olmkn', 'trpqs', 'xywuv'], "YES"), 
        (['ebacd', 'fghij', 'olmkn', 'arpqs', 'xywuv'], "NO"),  
       
    ]

    for grid, expected in test_cases:
        result = gridChallenge(grid)
        assert result == expected, f"Test with grid {grid} failed. Expected {expected}, got {result}."
        print(f"Test with grid {grid} passed. Expected and got {expected}.")

    print("All tests passed!")

if __name__ == '__main__':
    test_gridChallenge()
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    # t = int(input().strip())

    # for t_itr in range(t):
    #     n = int(input().strip())

    #     grid = []

    #     for _ in range(n):
    #         grid_item = input()
    #         grid.append(grid_item)

    #     result = gridChallenge(grid)

    #     fptr.write(result + '\n')

    # fptr.close()

