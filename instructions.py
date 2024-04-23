import pygame 

pygame.font.init()

screen_height = 768
screen_width = 1024
bounds = (screen_width, screen_height)
window = pygame.display.set_mode(bounds)
pygame.display.set_caption("Rat Slapper: Instructions")
green = (0, 255, 0)
blue = (0, 0, 128)

def instructions_screen():
    window.fill((202, 228, 241))

    fontHead = pygame.font.SysFont('comicsans', 60)
    fontBody = pygame.font.SysFont('comicsans', 30)
    textHead = fontHead.render("Instructions", True, (255,255,255))
    textBody = fontBody.render("meow meow meow\n cows cows cows\n", True, (255,255,255))

    window.blit(textHead, (200, 100))

    textRules = ["1. CATS",
                "2. DOGS"]
    
    yValue = 200

    for line in textRules: 
        ruleText = fontBody.render(line, True, (255,255,255))
        ruleCoord = (200, yValue)
        window.blit(ruleText, ruleCoord)

        yValue += 50 

    while True: 

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

        pygame.display.update()

instructions_screen()
                


