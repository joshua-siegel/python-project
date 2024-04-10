from enum import Enum
import pygame
import random

class Suits(Enum):
    CLUB = 0
    SPADE = 1
    HEART = 2
    DIAMOND = 3

### GAME MODELS ###

# Card Model
class Card:
    suit = None
    value = None
    image = None

    def __init__(self, suit, value):
        self.suit = suit
        self.value = value
        self.image = pygame.image.load('images/' + self.suit.name + '-' + str(self.value) + '.svg')

# Deck Model
class Deck:
    cards = None

    def __init__(self):
        self.cards = []
        for suit in Suits:
            for value in range(1,14):
                self.cards.append(Card(suit, value))

    # Shuffles deck
    def shuffle(self):
        random.shuffle(self.cards)

    # Deals last card from deck list (removes and returns)
    def deal(self):
        return self.cards.pop()

    # Determines length of deck
    def length(self):
        return len(self.cards)

# Pile Model
class Pile:
    cards = None

    def __init__(self):
        self.cards = []

    # Adds a card to the pile when someone plays from hand
    def add(self, card):
        self.cards.append(card)

    # Shows top card on pile
    def peek(self):
        if (len(self.cards) > 0):
            return self.cards[-1]
        else:
            return None

    # Returns pile to someone
    def popAll(self):
        return self.cards

    # Clears pile
    def clear(self):
        self.cards = []

    # Checks if slap is valid
    def isSlap(self, rules, mods):
        validity = []

        # 2 in a Row
        if (len(self.cards) > 1) and rules["2InARow"]:
            validity.append(self.cards[-1].value == self.cards[-2].value)

        # Sandwich 
        if (len(self.cards) > mods["sandLength"]) and rules["sandwich"]:
            validity.append(self.cards[-1].value == self.cards[-1 - mods["sandLength"]].value)

        # Add to 10
        if (len(self.cards) > 1) and rules["addTo10"]:
            validity.append(self.cards[-1].value + self.cards[-2].value == mods["addTo10Sum"])

        # 10 Sandwich
        if (len(self.cards) > mods["sand10Length"]) and rules["sandwich10"]:
            validity.append(self.cards[-1].value + self.cards[-1 - mods["sand10Length"]].value == mods["sand10Sum"])

        # Marriage
        if (len(self.cards) > 1) and rules["marriage"]:
            validity.append(self.cards[-1].value == mods["marDivCards"][0] and self.cards[-2].value == mods["marDivCards"][1])
            validity.append(self.cards[-1].value == mods["marDivCards"][1] and self.cards[-2].value == mods["marDivCards"][0])

        # Divorce
        if (len(self.cards) > mods["divSuitors"]) and rules["marriage"]:
            validity.append(self.cards[-1].value == mods["marDivCards"][0] and self.cards[-1 - mods["divSuitors"]].value == mods["marDivCards"][1])
            validity.append(self.cards[-1].value == mods["marDivCards"][1] and self.cards[-1 - mods["divSuitors"]].value == mods["marDivCards"][0])

        # Top Bottom
        if (len(self.cards) > 1) and rules["topBottom"]:
            validity.append(self.cards[-1].value == self.cards[0].value)

        # (EXTRA) Top Bottom: Addition
        if (len(self.cards) > 1) and rules["topBottom"]:
            validity.append(self.cards[-1].value + self.cards[0].value == mods["topBottomSum"])

        # (EXTRA) Top Bottom: Total Divorce
        if (len(self.cards) > 1) and rules["topBottom"]:
            validity.append(self.cards[-1].value == mods["marDivCards"][0] and self.cards[0].value == mods["marDivCards"][1])
            validity.append(self.cards[-1].value == mods["marDivCards"][1] and self.cards[0].value == mods["marDivCards"][0])

        # Consecutive 4
        if (len(self.cards) >= mods["consecLength"]) and rules["consec4"]:
            # Extract the last 4 Numbers
            lastFour = self.cards[-mods["consecLength"]:]

            # Check if the difference between adjacent numbers is 1 for ascending and descending
            if mods["ascending"]:
                if all(lastFour[i + 1].value - lastFour[i].value == 1 for i in range(mods["consecLength"] - 1)):
                    validity.append(True)
                        
            if mods["descending"]:
                if all(lastFour[i + 1].value - lastFour[i].value == -1 for i in range(mods["consecLength"] - 1)):
                    validity.append(True)

        return any(validity)
        
# Player Model
class Player:
    hand = None
    flipKey = None
    slapKey = None
    name = None

    def __init__(self, name, flipKey, slapKey):
        self.hand = []
        self.flipKey = flipKey
        self.slapKey = slapKey
        self.name = name

    # Draws card into hand from dealer
    def draw(self, deck):
        self.hand.append(deck.deal())

    # Plays card from hand
    def play(self):
        return self.hand.pop(0)



