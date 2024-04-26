from enum import Enum
import pygame
from models import *

class GameState(Enum):
    PLAYING = 0
    SLAPPING = 1
    FACE = 2
    ENDED = 3

class RatEngine:
    deck = None
    player1 = None
    player2 = None
    pile = None
    state = None
    currentPlayer = None
    result = None
    rules = None

    def __init__(self):
        self.deck = Deck()
        self.deck.shuffle()
        self.player1 = Player("Player 1", pygame.K_q, pygame.K_w)
        self.player2 = Player("Player 2", pygame.K_o,pygame.K_p)
        self.pile = Pile()
        self.deal()
        self.currentPlayer = self.player1
        self.state = GameState.PLAYING
        self.rules = Rules()

    # Deals the cards
    def deal(self):
        half = self.deck.length() // 2
        for i in range(0, half):
            self.player1.draw(self.deck)
            self.player2.draw(self.deck)

    # Switches player
    def switchPlayer(self):
        if self.currentPlayer == self.player1:
            self.currentPlayer = self.player2
        else:
            self.currentPlayer = self.player1

    # Handle when player wins a round
    def winRound(self, player):
        if self.pile.faceStatus(self.rules.faceRules, self.rules.faceMods) == "Over":
            self.state = GameState.FACE
        else: 
            self.state = GameState.SLAPPING
        player.hand.extend(self.pile.popAll())
        self.pile.clear()

    # Processes logic for key pressed
    def play(self, key):

        if key == None:
            return

        if self.state == GameState.ENDED:
            return

        # Check if Flip and Face Card Status
        if key == self.currentPlayer.flipKey:
            self.pile.add(self.currentPlayer.play())
            faceStatus = self.pile.faceStatus(self.rules.faceRules, self.rules.faceMods)
            if faceStatus != "On":
                self.switchPlayer()

        # Check is Slap is called
        slapCaller = None
        nonSlapCaller = None
        isSlap = self.pile.isSlap(self.rules.slapRules, self.rules.slapMods)

        if (key == self.player1.slapKey):
            slapCaller = self.player1
            nonSlapCaller = self.player2
        elif (key == self.player2.slapKey):
            slapCaller = self.player2
            nonSlapCaller = self.player1

        # Check Slap Result
        if isSlap and slapCaller:
            self.winRound(slapCaller)
            self.result = {
                "winner": slapCaller,
                "isSlap": True,
                "slapCaller": slapCaller
            }
            self.winRound(slapCaller)
        elif not isSlap and slapCaller:
            self.result = {
                "winner": nonSlapCaller,
                "isSlap": False,
                "slapCaller": slapCaller
            }
            self.winRound(nonSlapCaller)

        # Check if a player wins by face card rule
        if (not (isSlap and slapCaller)) and faceStatus == "Over":
            self.result = {
                "winner": self.currentPlayer,
            }
            self.winRound(self.currentPlayer)

        # Check if player runs out of cards
        if len(self.player1.hand) == 0:
            self.result = {
                "winner": self.player2,
            }
            self.state = GameState.ENDED
        elif len(self.player2.hand) == 0:
            self.result = {
                "winner": self.player1,
            }
            self.state = GameState.ENDED



    

