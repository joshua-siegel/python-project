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
        window.fill((100, 151, 243))
        font = pygame.font.SysFont('comicsans',50, True)
        font2 = pygame.font.SysFont('comicsans',25, True)

        window.blit(cardBack, (100, 200))
        window.blit(cardBack, (700, 200))

        text = font.render(str(len(gameEngine.player1.hand)) + " cards", True, (255,255,255))
        window.blit(text, (100, 500))

        text = font.render(str(len(gameEngine.player2.hand)) + " cards", True, (255,255,255))
        window.blit(text, (700, 500))

        # Player Key Directions
        Player1_label = font2.render("Player 1", True, (255,255,255))
        Player1_keys = font2.render("Q = Flip, W = Slap", True, (255,255,255))
        Player2_label = font2.render("Player 2", True, (255,255,255))
        Player2_keys = font2.render("O = Flip, P = Slap", True, (255,255,255))
        window.blit(Player1_keys, (100, 700))
        window.blit(Player2_keys, (700, 700))
        window.blit(Player1_label, (100, 650))
        window.blit(Player2_label, (700, 650))

        topCard = gameEngine.pile.peek()
        if (topCard != None):
            window.blit(topCard.image, (400, 200))

        # Indicate current state of game and whose turn it is
        if gameEngine.state == GameState.PLAYING:
            text = font.render(gameEngine.currentPlayer.name + " to flip", True, (255,255,255))
            window.blit(text, (100,50))

        if gameEngine.state == GameState.SLAPPING:
            result = gameEngine.result
            if result["isSlap"] == True:
                message = "Winning Slap! by " + result["winner"].name
            else:
                message = "False Slap! by " + result["slapCaller"].name + ". " + result["winner"].name + " wins!"
            text = font.render(message, True, (255,255,255))
            window.blit(text, (100,50))

        if gameEngine.state == GameState.FACE:
            result = gameEngine.result
            message = result["winner"].name + " wins by face card played!"
            text = font.render(message, True, (255,255,255))
            window.blit(text, (100,50))

        if gameEngine.state == GameState.ENDED:
            result = gameEngine.result
            message = "Game Over! " + result["winner"].name + " wins!"
            text = font.render(message, True, (255,255,255))
            window.blit(text, (100,50))

    # Run Game Loop (Listen for User Input, Process Input w/ Engine Play Method, Update UI w/ Result)
    run = True
    while run:
        key = None
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                break
            if event.type == pygame.KEYDOWN:
                key = event.key

        gameEngine.play(key)
        renderGame(window)
        pygame.display.update()

        if gameEngine.state == GameState.SLAPPING or gameEngine.state == GameState.FACE:
            pygame.time.delay(1000)
            gameEngine.state = GameState.PLAYING
    pygame.quit()
