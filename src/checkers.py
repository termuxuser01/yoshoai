#temporary file for functions that checki input, in the mean time
from src.resp_gen import *

def checker(input_st):
    if(UserDismiss(input_st)):
        quit = True
        return YoshoDismiss(), quit
    elif(lbomb(input_st)):
        return Yosholbomb(), False
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
        if(input_st.lower() == bye):
            return True
        else:
            continue

    return False

def lbomb(input_st):
    lb_comp = [
            "i", "love", "you"
            ]

    input_st = input_st.lower().split()

    result = all([(lb_comp[0] in input_st), (lb_comp[1] in input_st), (lb_comp[2] in input_st)])
    print(result)

    if(result):
        return True
    else:
        return False
