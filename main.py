from card_shuffler import *
if __name__ == '__main__':
    """
    __name__ is set to the name of script/module, which here is main
    __name__ == '__main__' implies that module is being run standalone by user
    .py files can be used as reusable modules or as standalone program
    """
    deck = Deck()
    deck.shuffle()

    deck.build()
    deck.show()

    print()
    k = deck.drawCard()
    k.show()
