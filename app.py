import random


class Cards:
    def __init__(self, value, suite):
        self.value = value
        self.suite = suite
        # self.face = face

    def show(self):
        print('{} of {}'.format(self.value, self.suite))


class Deck:
    def __init__(self):
        self.deck = []
        self.build()

    def build(self):
        for i in range(1, 14):
            for j in ["spade", "club", "heart", "diamond"]:
                self.deck.append(Cards(i, j))

    def show_deck(self):
        for cards in self.deck:
            cards.show()

    def shuffle(self):
        random.shuffle(self.deck)

    def draw_card(self):
        return self.deck.pop(0)

    def re_deck(self):
        self.deck.clear()
        self.build()


class People:
    def __init__(self, player_name):
        self.name = player_name


def deal(deck):
    dealer_hand = []
    player_hand = []
    dealer_hand.append(deck.draw_card())
    player_hand.append(deck.draw_card())
    dealer_hand.append(deck.draw_card())
    player_hand.append(deck.draw_card())
    print("***************************************")
    print("Dealer")
    dealer_hand[0].show()
    print("Total:")
    print("***************************************")
    print("Player")
    for card in player_hand:
        card.show()
    print("Total:")
    print("***************************************")


if __name__ == '__main__':
    d1 = Deck()
    d1.shuffle()
    asktoplay = input("Do you wanna bet?")
    if asktoplay in ["Y", "y", "YES", "Yes", "yes"]:
        deal(d1)

    elif asktoplay in ["N", "n", "NO", "No", "no"]:
        quit()
    else:
        pass

