import random


class Cards:
    def __init__(self, face, suite):
        self.face = face
        self.suite = suite
        if self.face in ["J", "Q", "K"]:
            self.value = 10
        elif self.face == "A":
            self.value = 1
        else:
            self.value = int(self.face)

    def show(self):
        return self.face, self.suite, self.value
        # print('{} of {}'.format(self.value, self.suite))


class Deck:
    def __init__(self):
        self.deck = []
        self.build()

    def build(self):
        for i in ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]:
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
        self.total = 0

    def show_player_hand(self):
        print(self.name)
        for cards in self.play_hand:
            print('{} of {}'.format(cards.face, cards.suite), end=", ")


class Dealer:
    def __init__(self, deal_hand):
        self.deal_hand = deal_hand
        self.total = 0

    def show_dealer_hand(self):
        print("Dealer")
        for cards in self.deal_hand:
            print('{} of {}'.format(cards.face, cards.suite), end=", ")


def hand_total(hand):
    total = 0
    for cards in hand:
        total = total + cards.value
    return total


def display(player, call_stand):
    if call_stand:
        print("***************************************")
        deal1.show_dealer_hand()
        print("\nTotal:", hand_total(deal1.deal_hand))
    else:
        print("***************************************")
        print("Dealer")
        print(deal1.deal_hand[0].show()[0], "of", deal1.deal_hand[0].show()[1])
        print("Total:", )
    print("***************************************")
    player.show_player_hand()
    print("\nTotal:", hand_total(player.play_hand))
    print("***************************************")


def stand(player):
    while hand_total(deal1.deal_hand) < 17:
        deal1.deal_hand.append(d1.draw_card())
    display(player, call_stand=1)
    if hand_total(deal1.deal_hand) > 21:
        print("Dealer Bust", player.name, "Wins!!!")
    elif hand_total(player.play_hand) > hand_total(deal1.deal_hand):
        print(player.name, "Wins!!!")
    elif hand_total(player.play_hand) < hand_total(deal1.deal_hand):
        print("Dealer Wins!!!")
    else:
        print("Push!!!")


def hit_or_stand(player):
    next_move = input("H: Hit, S: Stand, D: Double")
    while next_move not in ["S", "s", "STAND", "Stand", "stand"]:
        if next_move in ["H", "h", "HIT", "Hit", "hit"]:
            player.play_hand.append(d1.draw_card())
            display(player, call_stand=0)
            if hand_total(player.play_hand) <= 21:
                return hit_or_stand(player)
            else:
                print("Bust - You Loose")
                break
        elif next_move in ["D", "d", "DOUBLE", "Double", "double"]:
            player.play_hand.append(d1.draw_card())
            stand(player)
            break
        else:
            print("Invalid input. Please Try again.")
            next_move = input("H: Hit, S: Stand, D: Double")
    else:
        stand(player)
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
        display(p1, call_stand=0)
        hit_or_stand(p1)

    elif ask_to_play in ["N", "n", "NO", "No", "no"]:
        quit()
    else:
        pass
