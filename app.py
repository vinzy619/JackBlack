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


class Dealer:
    def __init__(self, deal_hand):
        self.deal_hand = deal_hand

    def show_dealer_hand(self):
        total = 0
        print("Dealer")
        for cards in self.deal_hand:
            print('{} of {}'.format(cards.value, cards.suite), end=", ")
            total = total + cards.value

        print("\nTotal:", total)


def display(dealer, player):
    print("***************************************")
    print("Dealer")
    print(dealer.deal_hand[0].show()[0], "of", dealer.deal_hand[0].show()[1])
    print("Total:", )
    print("***************************************")
    player.show_player_hand()
    print("***************************************")


def hit_or_stand(player):
    next_move = input("H: Hit, S: Stand, D: Double")
    while next_move not in ["S", "s", "STAND", "Stand", "stand"]:
        if next_move in ["H", "h", "HIT", "Hit", "hit"]:
            player.play_hand.append(d1.draw_card())
            display(deal1, p1)
            return hit_or_stand(player)
        if next_move in ["D", "d", "DOUBLE", "Double", "double"]:
            player.play_hand.append(d1.draw_card())
            display(deal1, p1)
            break
    else:
        print("Player Stands")
        return


if __name__ == '__main__':
    p1 = Player("John", play_hand=[])
    deal1 = Dealer(deal_hand=[])
    d1 = Deck()
    d1.shuffle()
    ask_to_play = input("Do you wanna bet?")
    if ask_to_play in ["Y", "y", "YES", "Yes", "yes"]:
        deal1.deal_hand.append(d1.draw_card())
        p1.play_hand.append(d1.draw_card())
        deal1.deal_hand.append(d1.draw_card())
        p1.play_hand.append(d1.draw_card())
        display(deal1, p1)
        hit_or_stand(p1)

    elif ask_to_play in ["N", "n", "NO", "No", "no"]:
        quit()
    else:
        pass
