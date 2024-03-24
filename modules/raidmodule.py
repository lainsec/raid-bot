import os
import sys
from cdn import __sdk
import platform

__doc__ = "This module was made to serve the main app"

def check_sys():
    sys = platform.system()
    if sys == 'Windows':
        return True
    else:
        return False

def clear_screen():
    if check_sys():
        os.system('cls')
        print(__sdk.banner)
    else:
        os.system('clear')
        print(__sdk.banner)




if __name__ == '__main__':
    print("This module shouldn't be open alone, please open the main app.")
