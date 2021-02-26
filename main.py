import pickle
import argparse
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer

#Initialize chatbot and specify database file
cb = ChatBot(
        "yosho",
        sotarge_adapter="chatterbot.storage.SQLStorageAdapter",
        )


def cchat(cb):
    while True:
        try:
            response = cb.get_response(input("You:"))
            print("Yosho:", response)
        except(KeyboardInterrupt, EOFError, SystemExit):
            print()
            print("Yosho: Bye masta!")
            break

if __name__ == "__main__":
    #handle arguments
    parser = argparse.ArgumentParser()
    parser.add_argument("--cchat", help="Chat from commandline",
            action="store_true")
    args = parser.parse_args()
    #end arguments

    if(args.cchat):
        cchat(cb)

    print("done!")
