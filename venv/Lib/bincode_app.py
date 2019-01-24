# ==================================================================
# title           :bincode_app 
# description     :
# author          :srattigan
# date            :24/01/2019
# version         :1.0
# notes           :change from last version
# python_version  :3.7  
# file_version    :1.00
# ==================================================================

# imports
import menugen
import bincode

# globals and constants


# functions


# main body

if __name__ == "__main__":
    bin_menu = menugen.Menu("Binary Encoder Decoder", ["Encode text to binary string", "Decode Binary to text", "Quit"])
    while True:
        response = bin_menu.display()
        if response == 0:
            print("Encode called")
        elif response == 1:
            print("Decode called")
        elif response == 2:
            break
        else:
            print("Something strange happened")