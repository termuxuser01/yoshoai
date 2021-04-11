import pickle
import argparse
from src.checkers import checker
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer

#Initialize chatbot and specify database file
cb = ChatBot(
        "yosho",
        sotarge_adapter="chatterbot.storage.SQLStorageAdapter",
        )

def generate_chat(cb, inpt):
    if((not checker(inpt)[0]) & (not checker(inpt)[1])):
        return cb.get_response(inpt), False
    elif((type(checker(inpt)) == str) & (not checker(inpt)[1])):
        return checker(inpt)
    else:
        response, quit = checker(inpt)
        return response, quit

def cchat(cb):
    while True:
        try:
            response, quit = generate_chat(cb, input("You:"))
            print("Yosho:", response)
            if(quit):
                raise KeyboardInterrupt
        except(KeyboardInterrupt, EOFError, SystemExit):
            break

if __name__ == "__main__":
    #handle arguments
    parser = argparse.ArgumentParser()
    parser.add_argument("--cchat", help="Chat from commandline",
            action="store_true")
    parser.add_argument("--discord", help="Start the discord bot",
            action ="store_true")
    parser.add_argument("-v", "--verbose", help="Have verbose output",
            action="store_true")
    args = parser.parse_args()
    #end arguments

    if(args.cchat):
        cchat(cb)
    elif(args.discord):
        from servers.discord_handler import *
        discord_chat(client, discord_key, cb, generate_chat, args.verbose) 

    print("done!")
