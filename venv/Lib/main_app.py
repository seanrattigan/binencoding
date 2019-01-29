# ==================================================================
# title           :main_app 
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
import duckode_app as duk
import bincode_app as bin

# globals and constants


# functions


# main body


if __name__ == "__main__":
    bin_menu = menugen.Menu("Master Program", ["Work with bincoding", "Work with duckoding", "Quit"])
    while True:
        response = bin_menu.display()
        if response == 0:
            # print("bincoder app call")
            bin.bin_app()
        elif response == 1:
            # print("duckoder app call")
            duk.duk_app()
        elif response == 2:
            break
        else:
            print("Something strange happened")
