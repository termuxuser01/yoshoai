#temporary file for functions that checki input, in the mean time
from src.resp_gen import *

def checker(input_st):
    if(UserDismiss(input_st)):
        quit = True
        return YoshoDismiss(), quit
    else:
        quit = False
        return False, quit

def UserDismiss(input_st):
    """Function to check if user says good bye"""
    byes = [
            "bye", "good bye", "see you",
            "farewell", "take care", "bye now",
            "ciao", "bye now"
            ]
    for bye in byes:
        if(input_st == bye):
            return True
        else:
            continue

    return False

