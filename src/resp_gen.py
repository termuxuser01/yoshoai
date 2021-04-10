import random

def YoshoDismiss():
    yoshobyes = [
            "see ya masta!", "I'll miss you!",
            "aww do you have to go?!"
            ]
    
    return yoshobyes[random.randrange(len(yoshobyes))]
