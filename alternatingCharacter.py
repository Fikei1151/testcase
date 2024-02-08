#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'alternatingCharacters' function below.
#
# The function is expected to return an INTEGER.
# The function accepts STRING s as parameter.
#

def alternatingCharacters(s):

    deletions = 0
    for i in range(len(s) - 1):

        if s[i] == s[i + 1]:
            deletions += 1
            
    return deletions

def run_test_cases():
    test_cases = [
        ("AAAA", 3),  
        ("BBBBB", 4),  
        ("ABABABAB", 0),  
        ("BABABA", 0),  
        ("AAABBB", 4),  
        ("", 0), 
        ("A", 0),  
        ("A"*1000, 999),  
        ("AB"*500, 0),  
    ]
    
    for s, expected_deletions in test_cases:
        result = alternatingCharacters(s)
        assert result == expected_deletions, f"Test case for string '{s}' failed: expected {expected_deletions} deletions, got {result}"
        print(f"Test case for string '{s}' passed: expected and got {expected_deletions} deletions")

if __name__ == '__main__':
    run_test_cases()
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    # q = int(input().strip())

    # for q_itr in range(q):
    #     s = input()

    #     result = alternatingCharacters(s)

    #     fptr.write(str(result) + '\n')

    # fptr.close()
