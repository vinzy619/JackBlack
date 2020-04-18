import random


number = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "A", "J", "Q", "K"]
suite = ["spade", "club", "heart", "diamond"]

deck = [v + " of " + w for v in number for w in suite]
print(deck)

print(random.choice(deck))
