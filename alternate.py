#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'alternate' function below.
#
# The function is expected to return an INTEGER.
# The function accepts STRING s as parameter.
#
def alternate(s):
    unique_chars = list(set(s))
    max_length = 0


    for i in range(len(unique_chars)):
        for j in range(i + 1, len(unique_chars)):
        
            pair = {unique_chars[i], unique_chars[j]}
            filtered_string = [c for c in s if c in pair]
            if all(filtered_string[k] != filtered_string[k + 1] for k in range(len(filtered_string) - 1)):
                max_length = max(max_length, len(filtered_string))

    return max_length

def run_test_cases():
    test_cases = [
        ("beabeefeab", 5),  
        ("aabbcc", 0),  
        ("aaaa", 0),  
        ("ababab", 6), 
        ("", 0),  
        ("ababababababababababa", 21),
          ("xyxyxyx", 7)  
       
    ]
    
    for s, expected in test_cases:
        result = alternate(s)
        assert result == expected, f"Test with '{s}': Expected {expected}, got {result}"
        print(f"Test with '{s}' passed. Expected and got {expected}.")



if __name__ == '__main__':
    run_test_cases()
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    # l = int(input().strip())

    # s = input()

    # result = alternate(s)

    # fptr.write(str(result) + '\n')

    # fptr.close()
