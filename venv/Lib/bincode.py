# ==================================================================
# title           :bincode 
# description     :
# author          :srattigan
# date            :24/01/2019
# version         :1.0
# notes           :draft
# python_version  :3.7  
# file_version    :1.00
# ==================================================================

# imports
import menugen

# globals and constants


# functions
def encode(plaintext):
    """
    (str)->str
    takes plain text and converts to a binary code format
    >>> encode("b")
    '1100010'
    >>> encode("bad")
    '1100010/1100001/1100100'
    """
    if len(plaintext) < 1:
        print("No data detected!")
        return ""
    if type(plaintext) != str:
        raise TypeError("Non-str object cannot be encoded!")
    else:
        cypher = ""
        for ch in plaintext:
            cypher += str(bin(ord(ch)))[2:] + "/"
    return cypher[:-1]  # to drop the last '/'


def decode(cyphertext):
    """
    (str)->str
    takes binary nums and converts to chars
    >>> decode('1000010')
    'b'
    >>> encode('1000010/1000001/1100100')
    'bad
    """
    if type(cyphertext) != str:
        raise TypeError("Non-str object cannot be encoded!")
    plain = ""  # initialises empty str
    if len(cyphertext) < 1:
        print("No data detected!")
        return plain
    else:
        bitlist = cyphertext.split('/')  # creates list of bytes
        # print(bitlist)  # debug
        for bits in bitlist:  # iterator for bytes
            plain += chr(int(bits, 2))  # converts back to char
    return plain

# main body

if __name__ == "__main__":
    print("\n\tTesting Encode function...\n")
    a1 = encode("a")
    print(a1)
    a2 = encode("abc")
    print(a2)
    a3 = encode("The cat sat on the mat")
    print(a3)
    a4 = encode("A cat ate 5 eggs @ 10:45!")
    print(a4)
    print("*" * 30 + "\n\tTesting Decode Function\n")
    print(decode(a1))
    print(decode(a2))
    print(decode(a3))
    print(decode(a4))
