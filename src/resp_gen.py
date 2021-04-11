import random

def YoshoDismiss():
    yoshobyes = [
            "see ya masta!", "I'll miss you!",
            "aww do you have to go?!"
            ]
    
    return yoshobyes[random.randrange(len(yoshobyes))]

def Yosholbomb():
    yosho = [
            "W-why master, I'm blushing!", "I love you too master!",
            "I will always love you master!"
            ]
    return yosho[random.randrange(len(yosho))]
