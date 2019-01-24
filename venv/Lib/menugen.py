# ==================================================================
# title           :menugen 
# description     :
# author          :srattigan
# date            :24/01/2019
# version         :1.0
# notes           :change from last version
# python_version  :3.7  
# file_version    :1.00
# ==================================================================

# imports
import time
import os

# globals and constants
delay = 1.5
clr = 'cls' # string to clear the screen in os.system (Windows)
# if os is linux /OSx change call to the Unix-type clear
if os.name == 'posix':
    clr = 'clear'

# functions

class Menu:
    '''
    Creates an instance of a menu for command line programs
    A Menu has a title and a list of options
    '''
    def __init__(self, the_title, the_options):
        '''
        (str, list of str)-> None
        Creates a menu
        '''
        self.title = the_title
        self.options = the_options

    def display(self):
        '''
        (None) -> int
        Centers the title on the screen
        Creates a menu from the list items and returns the index of
        the item chosen by the user
        Handles bad and invalid input from the user and loops
        until a valid selection is made
        '''
        os.system(clr)  # clear the screen
        spaces = 40 - (len(self.title) // 2)
        while True:
            print("\n" + (" " * spaces) + self.title + "\n")
            for i in range(len(self.options)):
                print("\t" + str(i + 1) + ") " + str(self.options[i]))
            selected = input("\nEnter your selection: ")
            try:
                selected = int(selected)
                if selected in range(1, len(self.options) + 1):
                    return selected - 1
                else:
                    print("Value entered was not in the menu:")
                    time.sleep(delay)
            except:
                print("Non-numerical value entered: Please try again")
                time.sleep(delay)


if __name__ == "__main__":
    # shows simple demo of using the Menu class with one method
    test1 = Menu("Testing Class Menu", ["Item A", "Item B", "Item C"])
    response = test1.display()
    print(response)
