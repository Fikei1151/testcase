#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'caesarCipher' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. STRING s
#  2. INTEGER k
#

def caesarCipher(s, k):

    encrypted = ""

    for char in s:
        if char.isalpha():
            first = ord('a') if char.islower() else ord('A')
            alpha_index = ord(char) - first
            rotated_index = (alpha_index + k) % 26
            encrypted_char = chr(rotated_index + first)
            encrypted += encrypted_char
        else:
            encrypted += char
            
    return encrypted

def run_test_cases():
    test_cases = [
        ("middle-Outz", 2, "okffng-Qwvb"),  
        ("Hello-World!", 4, "Lipps-Asvph!"),  
        ("abc", 3, "def"),  
        ("xyz", 3, "abc"), 
        ("XYZ", 3, "ABC"),  
        ("Hello, World!", 26, "Hello, World!"),  
        ("", 5, ""), 
        ("12345!@#$%", 10, "12345!@#$%"),  
        ("abc", 0, "abc"), 
        ("abc", 52, "abc"),  
    ]
    
    for s, k, expected in test_cases:
        result = caesarCipher(s, k)
        assert result == expected, f"Test case for string '{s}' with rotation '{k}' failed: expected '{expected}', got '{result}'"
        print(f"Test case for string '{s}' with rotation '{k}' passed: expected and got '{expected}'")


if __name__ == '__main__':
    run_test_cases()
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    # n = int(input().strip())

    # s = input()

    # k = int(input().strip())

    # result = caesarCipher(s, k)

    # fptr.write(result + '\n')

    # fptr.close()
