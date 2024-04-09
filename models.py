from enum import Enum
import pygame
import random

class Suits(Enum):
    CLUB = 0
    SPADE = 1
    HEART = 2
    DIAMOND = 3

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

    # Checks if snap is valid
    def isSnap(self):
        if (len(self.cards) > 1):
            return (self.cards[-1].value == self.cards[-2].value)
        return False

class Player:
    hand = None
    flipKey = None
    snapKey = None
    name = None

    def __init__(self, name, flipKey, snapKey):
        self.hand = []
        self.flipKey = flipKey
        self.snapKey = snapKey
        self.name = name

    # Draws card into hand from dealer
    def draw(self, deck):
        self.hand.append(deck.deal())

    # Plays card from hand
    def play(self):
        return self.hand.pop(0)
