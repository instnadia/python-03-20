class Card:
    def __init__(self, suit, val):
        self.suit = suit
        self.val = val

        if(val==1):
            self.name ="Ace"
        elif(val==11):
            self.name = "Jack"
        elif(val==12):
            self.name = "Queen"
        elif(val==13):
            self.name = "King"
        else:
            self.name = str(val)
        
    def __repr__(self):
        return f"{self.name} of {self.suit}"

# jack_of_hearts = Card("Hearts", 11)

#  without __repr__ <__main__.Card object at 0x0000025317BD9470>
# print(jack_of_hearts)

class Deck:
    def __init__(self):
        self.deck_of_cards = []

        suits = {"Hearts", "Clubs", "Diamonds", "Spades"}

        for suit in suits:
            for i in range(1,14):
                new_card = Card(suit, i)
                self.deck_of_cards.append(new_card)
        
    def print_deck(self):
        for card in self.deck_of_cards:
            print(card)

deck = Deck()
deck.print_deck()
