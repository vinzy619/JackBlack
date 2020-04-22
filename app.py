import random


class Cards:
    def __init__(self, value, suite):
        self.value = value
        self.suite = suite
        # self.face = face

    def show(self):
        return self.value, self.suite
        # print('{} of {}'.format(self.value, self.suite))


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


class Player:
    def __init__(self, play_name, play_hand):
        self.name = play_name
        self.play_hand = play_hand

    def show_player_hand(self):
        total = 0
        print(self.name)
        for cards in self.play_hand:
            print('{} of {}'.format(cards.value, cards.suite), end=", ")
            total = total + cards.value

        print("\nTotal:", total)


def deal(deck, player):
    dealer_hand = []
    dealer_hand.append(deck.draw_card())
    player.play_hand.append(deck.draw_card())
    dealer_hand.append(deck.draw_card())
    player.play_hand.append(deck.draw_card())
    print("***************************************")
    print("Dealer")
    print(dealer_hand[0].show()[0], "of", dealer_hand[0].show()[1])
    print("Total:", )
    print("***************************************")
    player.show_player_hand()
    print("***************************************")


if __name__ == '__main__':
    p1 = Player("John", play_hand=[])
    d1 = Deck()
    d1.shuffle()
    asktoplay = input("Do you wanna bet?")
    if asktoplay in ["Y", "y", "YES", "Yes", "yes"]:
        deal(d1, p1)

    elif asktoplay in ["N", "n", "NO", "No", "no"]:
        quit()
    else:
        pass

