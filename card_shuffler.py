import random
class Card():
    def __init__(self, value, suit):
        self.suit = suit
        self.value = value

    def show(self):
        print(f"{self.value} of {self.suit}")

class Deck():
    def __init__(self):
        self.cards = []
        self.build()

    def build(self):
        #builds a deck in order
        for s in ["Hearts", "Clubs", "Diamonds", "Spades"]:
            for v in range(1, 14):
                if v == 1:
                    v = "Ace"
                if v == 11:
                    v = "Jack"
                if v == 12:
                    v = "Queen"
                if v == 13:
                    v = "King"
                self.cards.append(Card(v, s))

    def show(self):
        count = 1
        for c in self.cards:
            print(count, end='. ')
            c.show()
            if count >= 52:
                print()
                count = 0
            count += 1

    def shuffle(self):
        # using Fisher-Yates Shuffle Algorithm
        # This algorithm simply places, the item in i in a random place r, and back
        for i in range(len(self.cards) - 1, 0, -1):
            r = random.randint(0, i)
            self.cards[i], self.cards[r] = self.cards[r], self.cards[i]

    def drawCard(self):
        r = random.randint(0,51)
        return self.cards.pop(r)

class Player():
    def __init__(self, name):
        self.name = name
        self.hand = []

    def draw(self, the_deck):
        self.hand.append(the_deck.drawCard())
        return self

    def showHand(self):
        for card in self.hand:
            card.show()

    def discard(self):
        return self.hand.pop()