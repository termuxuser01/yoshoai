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

def corpus_trainer(cb, cpt, custom):
    from chatterbot.trainers import ChatterBotCorpusTrainer
    
    trainer = ChatterBotCorpusTrainer(cb)

    if(bool(custom)):
        for mode in custom.split():
            try:
                trainer.train("chatterbot.corpus.english.{}".format(mode))
            except(FileNotFoundError):
                from wasabi import Printer
                msg = Printer()
                msg.fail("That corpus doesn't exist!")
                return -1

        print("all done training masta!")
    elif(bool(cpt)):
        trainer.train("chatterbot.corpus.english")
        print("all done training masta!")



if __name__ == "__main__":
    #handle arguments
    parser = argparse.ArgumentParser()
    parser.add_argument("-i", "--interactive", help="Interactive training from cli",
            action="store_true")
    parser.add_argument("--dp", help="dump pickle file to see stored data",
            action="store_true")
    
    #corpus arguments
    parser.add_argument("--corpus", action="store_true")
    parser.add_argument("--custom", type=str)
    #end corpus arguments

    args = parser.parse_args()
    #end handle arguments


    if(args.interactive):
        train_from_input(cb)

    if(args.dp):
        debug_pickle()

    #check corpus args

    if(bool(args.custom)):
        if(not bool(args.corpus)):
                from src.errors import CorpusArgs
                raise CorpusArgs("--corpus was not set see --help")
        else:
            corpus_trainer(cb, args.corpus, args.custom)
    else:
        corpus_trainer(cb, args.corpus, args.custom)
    #end check corpus args
