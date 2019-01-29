# ==================================================================
# title           :test_bincode 
# description     :
# author          :srattigan
# date            :24/01/2019
# version         :1.0
# notes           :change from last version
# python_version  :3.7  
# file_version    :1.00
# ==================================================================

# imports
from bincode import *

# globals and constants


# functions


# main body

if __name__ == "__main__":

    # can place all test cases in a single list for testing functions
    strings = ["a",
               "abc",
               "The cat sat on the mat",
               "A cat ate 5 eggs @ 10:45!"
               ]
    bits = []
    print("\n\tTesting Encode function...\n")
    for test_str in strings:
        coded = (encode(test_str))
        bits.append(coded)  # stores encoded data for decoding later
        print(coded)   # prints val returned from encode

    print("*" * 30 + "\n\n\tTesting Decode Function\n")
    for bitstrs in bits:
        print(decode(bitstrs))
