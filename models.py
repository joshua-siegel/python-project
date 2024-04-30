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

    # Check Face Card Status (Off, On, and Over)
    def faceStatus(self, rules, mods):
        # Create list of card values
        cardValues = [card.value for card in self.cards]
        print(cardValues)
        
        # Determine Active Face Card Rule
        if (len(cardValues) > 0):
            # Find most recent face card value if one exists in the pile, status is off if none exist in pile
            faceValues = [value for value in cardValues if value in rules.values()]
            if len(faceValues) > 0:
                mostRecent = faceValues[-1]
            else:
                print("Off")
                return "Off"

            # Correspond most recent face card value with active face card rule
            activeFace = [rule for rule in rules if rules[rule] == mostRecent][0]
            print(activeFace)

            # Rule Execution
            if activeFace == "stopper" or cardValues[-1] == mostRecent:
                print("Off")
                return "Off"

            for rule in rules:
                if rule == "stopper":
                    continue
                if activeFace == rule:
                    playChances = mods[rule]
                    chancesPlayed = cardValues[::-1].index(rules[rule])
                    if playChances - chancesPlayed > 0:
                        print("On")
                        return "On"
                    print("Over")
                    return "Over"

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

# Rules Model
class Rules:
    slapRules = None
    slapMods = None
    faceRules = None
    faceMods = None

    def __init__(self):
        self.slapRules = {
            "2InARow": True,
            "sandwich": True,
            "addTo10": False,
            "sandwich10": False,
            "marriage": False,
            "divorce": False,
            "topBottom": False,
            "topBottomAdd": False,
            "topBottomDiv": False,
            "consec4": False
            }
        self.slapMods = {
            "sandLength": 2,
            "addTo10Sum": 10,
            "sand10Length": 2,
            "sand10Sum": 10,
            "marDivCards": [12, 13],
            "divSuitors": 2,
            "topBottomSum": 10,
            "consecLength": 4,
            "ascending": True,
            "descending": True
            }
        self.faceRules = {
            "jack": 11,
            "queen": 12,
            "king": 13,
            "ace": 1,
            "stopper": 10
            }
        self.faceMods = {
            "jack": 1,
            "queen": 2,
            "king": 3,
            "ace": 4,
            }
    
    def slapRuleToggle(self, rule, state):
        self.slapRules[rule] = state

    def slapModToggle(self, mod, num):
        self.slapMods[mod] = num

# Button Model
class Button():
	def __init__(self, x, y, image, scale):
		width = image.get_width()
		height = image.get_height()
		self.image = pygame.transform.scale(image, (int(width * scale), int(height * scale)))
		self.rect = self.image.get_rect()
		self.rect.topleft = (x, y)
		self.clicked = False

	def draw(self, surface):
		
		action = False
		#get mouse position
		pos = pygame.mouse.get_pos()

		#check mouseover and clicked conditions
		if self.rect.collidepoint(pos):
			if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
				self.clicked = True
				action = True

		if pygame.mouse.get_pressed()[0] == 0:
			self.clicked = False

		#draw button on screen
		surface.blit(self.image, (self.rect.x, self.rect.y))

		return action
	
	def checkForInput(self, position):
		if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top, self.rect.bottom):
			return True
		return False












