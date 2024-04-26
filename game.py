import pygame
from models import *
from engine import *

screen_height = 768
screen_width = 1024
bounds = (screen_width, screen_height)
window = pygame.display.set_mode(bounds)
pygame.display.set_caption("Rat Slapper")

def game_screen():
    gameEngine = RatEngine()
    # pile = 
    Pile()
    # rules = 
    Rules()

    # Load back of card image
    cardBack = pygame.image.load('images/BACK.png')
    cardBack = pygame.transform.scale(cardBack, (int(238*0.8), int(332*0.8)))

    # Draws appropriate UI to window based on state and result of gameEngine
    def renderGame(window):
        # Draw general UI
        window.fill((202, 228, 241))
        font = pygame.font.SysFont('comicsans',60, True)

        window.blit(cardBack, (100, 200))
        window.blit(cardBack, (700, 200))

        text = font.render(str(len(gameEngine.player1.hand)) + " cards", True, (255,255,255))
        window.blit(text, (100, 500))

        text = font.render(str(len(gameEngine.player2.hand)) + " cards", True, (255,255,255))
        window.blit(text, (700, 500))

        topCard = gameEngine.pile.peek()
        if (topCard != None):
            window.blit(topCard.image, (400, 200))

        # Indicate current state of game and whose turn it is
        if gameEngine.state == GameState.PLAYING:
            text = font.render(gameEngine.currentPlayer.name + " to flip", True, (255,255,255))
            window.blit(text, (20,50))

        if gameEngine.state == GameState.SLAPPING:
            result = gameEngine.result
            if result["isSlap"] == True:
                message = "Winning Slap! by " + result["winner"].name
            else:
                message = "False Slap! by " + result["slapCaller"].name + ". " + result["winner"].name + " wins!"
            text = font.render(message, True, (255,255,255))
            window.blit(text, (20,50))

        if gameEngine.state == GameState.FACE:
            result = gameEngine.result
            message = result["winner"].name + " wins by face card played!"
            text = font.render(message, True, (255,255,255))
            window.blit(text, (20,50))

        if gameEngine.state == GameState.ENDED:
            result = gameEngine.result
            message = "Game Over! " + result["winner"].name + " wins!"
            text = font.render(message, True, (255,255,255))
            window.blit(text, (20,50))

    # Run Game Loop (Listen for User Input, Process Input w/ Engine Play Method, Update UI w/ Result)
    run = True
    while run:
        key = None
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
            if event.type == pygame.KEYDOWN:
                key = event.key

        gameEngine.play(key)
        renderGame(window)
        pygame.display.update()

        if gameEngine.state == GameState.SLAPPING or gameEngine.state == GameState.FACE:
            pygame.time.delay(3000)
            gameEngine.state = GameState.PLAYING
