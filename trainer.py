import argparse
import pickle
from main import cb

def train_from_input(cb):
    from chatterbot.trainers import ListTrainer
    with open("data/training.data", 'rb') as f:
        try:
            lst = pickle.load(f)
        except:
            lst = []

        print("I\'m ready for my training masta!")
        while True:
            try:
                lst.append(input("You say:"))
                lst.append(input("I say:"))
            except(KeyboardInterrupt, EOFError):
                print("Thank you masta!")
                break

        print("Give me a sec will ya?")
        trainer = ListTrainer(cb)
        trainer.train(lst)
        print("Yum that was some good data masta, thank you!")

    with open("data/training.data", 'wb') as f:
        pickle.dump(lst, f)

def debug_pickle():
    with open("data/training.data", 'rb') as f:
        lst = pickle.load(f)
        print(lst)

def train_corpus(cb):
    pass


if __name__ == "__main__":
    #handle arguments
    parser = argparse.ArgumentParser()
    parser.add_argument("-i", "--interactive", help="Interactive training from cli",
            action="store_true")
    parser.add_argument("--dp", help="dump pickle file to see stored data",
            action="store_true")
    args = parser.parse_args()
    #end handle arguments


    if(args.interactive):
        train_from_input(cb)

    if(args.dp):
        debug_pickle()
