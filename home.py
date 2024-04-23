import pygame
from models import *
from game import * 

pygame.init()

screen_height = 768
screen_width = 1024
bounds = (screen_width, screen_height)
window = pygame.display.set_mode(bounds)
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
	
	window.fill((202, 228, 241))
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
				# if OPTIONS_BUTTON.checkForInput(MENU_MOUSE_POS):
				# 	options()
				# if QUIT_BUTTON.checkForInput(MENU_MOUSE_POS):
				# 	pygame.quit()
				# 	sys.exit()

		pygame.display.update()

def play_game():
	game_screen()

main_menu()
pygame.quit()
