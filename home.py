import pygame
from models import *
from game import * 

pygame.init()

screen_height = 768
screen_width = 1024
bounds = (screen_width, screen_height)
window = pygame.display.set_mode(bounds)

# colors 
backgroundColor = (202, 228, 241)
white = (255,255,255)
green = (0, 255, 0)
blue = (0, 0, 128)


pygame.display.set_caption("Rat Slapper")


def main_menu():
	# logo image
	logo_img = pygame.image.load('images/logo.png')
	logo_img = pygame.transform.scale(logo_img, (850, 300))

	#load button images
	play_img = pygame.image.load('images/play.png').convert_alpha()
	rules_img = pygame.image.load('images/rules.png').convert_alpha()

	#create button instances
	play_button = Button(100, 400, play_img, 0.5)
	rules_button = Button(600, 400, rules_img, 0.5)
	
	window.fill(backgroundColor)
	window.blit(logo_img, (100,100))

	# game loop 
	run = True 
	while run:

		MENU_MOUSE_POS = pygame.mouse.get_pos()

		if play_button.draw(window):
			print('PLAY')
		if rules_button.draw(window):
			print('RULES')

		#event handler
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
			if event.type == pygame.MOUSEBUTTONDOWN:
				if play_button.checkForInput(MENU_MOUSE_POS):
					play_game()
					run = False
			if event.type == pygame.MOUSEBUTTONDOWN:
				if rules_button.checkForInput(MENU_MOUSE_POS):
					show_instructions()
					# run = False
				# if OPTIONS_BUTTON.checkForInput(MENU_MOUSE_POS):
				# 	options()
				# if QUIT_BUTTON.checkForInput(MENU_MOUSE_POS):
				# 	pygame.quit()
				# 	sys.exit()

		pygame.display.update()

def play_game():
	game_screen()

def show_instructions():
	window.fill((202, 228, 241))

	fontHead = pygame.font.SysFont('comicsans', 60)
	fontBody = pygame.font.SysFont('comicsans', 30)
	textHead = fontHead.render("Instructions", True, (255,255,255))
	textBody = fontBody.render("meow meow meow\n cows cows cows\n", True, (255,255,255))

	#load button 
	back_btn_img = pygame.image.load('images/backbtn.png').convert_alpha()

	#create button instances
	back_button = Button(100, 600, back_btn_img, 0.5)

	window.blit(textHead, (100, 100))

	textRules = ["1. CATS",
				"2. DOGS"]
	
	yValue = 200

	for line in textRules: 
		ruleText = fontBody.render(line, True, (255,255,255))
		ruleCoord = (100, yValue)
		window.blit(ruleText, ruleCoord)

		yValue += 50 

	run = True

	while run: 

		MENU_MOUSE_POS = pygame.mouse.get_pos()

		if back_button.draw(window):
			print('BACK')
					
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
			if event.type == pygame.MOUSEBUTTONDOWN:
				if back_button.checkForInput(MENU_MOUSE_POS):
					main_menu()

		pygame.display.update()


main_menu()
pygame.quit()
