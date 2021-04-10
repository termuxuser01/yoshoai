from difflib import SequenceMatcher

a = "bye"
b = "Good Bye"

print(SequenceMatcher(None, a, b).ratio())
