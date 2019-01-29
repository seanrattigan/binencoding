# ==================================================================
# title           :duckode_app 
# description     :
# author          :srattigan
# date            :29/01/2019
# version         :1.0
# notes           :change from last version
# python_version  :3.7  
# file_version    :1.00
# ==================================================================

# imports
import menugen
import duckode

# globals and constants


# functions
def get_string(opt=""):
    """
    (None)->str
    Gets a string from the user and returns it
    Takes an optional arguement that the caller can set
    """
    text = input(f"Enter string {opt}: ")
    return text


# main body

if __name__ == "__main__":
    bin_menu = menugen.Menu("Duck Encoder Decoder", ["Encode text to duckspeak", "Decode duckspeak to text", "Quit"])
    while True:
        response = bin_menu.display()
        if response == 0:
            print("Encode to duck called")  # may be commented out afterwards?
            cyph = duckode.encode(get_string("to encode text to duck"), get_string("for key"),  )
            print(cyph)
        elif response == 1:
            print("Decode called")  # may be commented out afterwards?
            plain = duckode.decode(get_string("to decode duck ro text"), get_string("for key"), )
            print(plain)
        elif response == 2:
            break
        else:
            print("Something strange happened")