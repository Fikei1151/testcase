#!/bin/python3

import math
import os
import random
import re
import sys



def funnyString(s):
    ascii_values = [ord(c) for c in s]
    differences = [abs(ascii_values[i] - ascii_values[i+1]) for i in range(len(ascii_values) - 1)]

    return "Funny" if differences == differences[::-1] else "Not Funny"

def run_test_cases():
    test_cases = [
        ("acxz", "Funny"),
        ("bcxz", "Not Funny"),
        ("aa", "Funny"),
        ("ab", "Funny"),
        ("aba", "Funny"),
        ("#@", "Funny"),
        ("", "Funny"),
        ("a", "Funny"),
        ("qwertyuiopasdfghjklzxcvbnmqwertyuiopasdfghjklzxcvbnm", "Not Funny"),
    ]
    
    for s, expected in test_cases:
        result = funnyString(s)
        assert result == expected, f"Test case for string '{s}' failed: expected {expected}, got {result}"
        print(f"Test case for string '{s}' passed: expected {expected}, got {result}")


if __name__ == '__main__':
    run_test_cases()
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    # q = int(input().strip())

    # for q_itr in range(q):
    #     s = input()

    #     result = funnyString(s)

    #     fptr.write(result + '\n')

    # fptr.close()
