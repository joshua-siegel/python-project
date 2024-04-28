import pygame
from models import *
from game import * 


pygame.init()
game_rules = Rules()

screen_height = 768
screen_width = 1024
bounds = (screen_width, screen_height)
window = pygame.display.set_mode(bounds)

# colors / aesthetics
backgroundColor = (202, 228, 241)
white = (255,255,255)
black = (0, 0, 0)
gray = (200, 200, 200)
green = (0, 255, 0)
blue = (0, 0, 128)

fontHead = pygame.font.SysFont('comicsans', 60)
fontBody = pygame.font.SysFont('comicsans', 30)
font = pygame.font.SysFont('comicsans', 20)

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
				run = False
				break

			if event.type == pygame.MOUSEBUTTONDOWN:
				if play_button.checkForInput(MENU_MOUSE_POS):
					play_game()
					run = False
			if event.type == pygame.MOUSEBUTTONDOWN:
				if rules_button.checkForInput(MENU_MOUSE_POS):
					show_instructions()

		pygame.display.flip()
	pygame.quit()

def play_game():
	configuration_screen()

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

def configuration_screen():
	window.fill((202, 228, 241))

	textHead = fontHead.render("Rule Modifications", True, (255,255,255))

	#load button 
	play_img = pygame.image.load('images/play.png').convert_alpha()

	#create button instances
	play_button = Button(700, 500, play_img, 0.4)

	window.blit(textHead, (100, 50))

	# Toggle buttons
 
	toggle_rect_2InARow = {
		'shape': pygame.Rect(100, 200, 100, 30),
		'state': False,
		'text': 'On',
		'rule': '2InARow'
	}
	toggle_rect_sandwich = {
		'shape': pygame.Rect(100, 250, 100, 31),
		'state': False,
		'text': 'On',
		'rule': 'sandwich'
	}
	toggle_rect_addTo10 = {
		'shape': pygame.Rect(100, 300, 100, 32),
		'state': False,
		'text': 'On',
		'rule': 'addTo10'
	}		
	toggle_rect_sandwich10 = {
		'shape': pygame.Rect(100, 350, 100, 33),
		'state': False,
		'text': 'On',
		'rule': 'sandwich10'
	}
	toggle_rect_marriage = {
		'shape': pygame.Rect(100, 400, 100, 34),
		'state': False,
		'text': 'On',
		'rule': 'marriage'
	}
	toggle_rect_divorce = {
		'shape': pygame.Rect(100, 450, 100, 35),
		'state': False,
		'text': 'On',
		'rule': 'divorce'
	}
	toggle_rect_topBottom = {
		'shape': pygame.Rect(100, 500, 100, 36),
		'state': False,
		'text': 'On',
		'rule': 'topBottom'
	}
	toggle_rect_topBottomAdd = {
		'shape': pygame.Rect(100, 550, 100, 37),
		'state': False,
		'text': 'On',
		'ruke': 'topBottomAdd'
	}
	toggle_rect_topBottomDiv = {
		'shape': pygame.Rect(100, 600, 100, 38),
		'state': False,
		'text': 'On',
		'rule': 'topBottomDiv'
	}
	toggle_rect_consec4 = {
		'shape': pygame.Rect(100, 650, 100, 39),
		'state': False,
		'text': 'On',
		'rule': 'consec4'
	}

	toggle_buttons = [toggle_rect_2InARow, toggle_rect_sandwich, 
			toggle_rect_addTo10, toggle_rect_sandwich10, 
			toggle_rect_marriage, toggle_rect_divorce,
			toggle_rect_topBottom, toggle_rect_topBottomAdd, 
			toggle_rect_topBottomDiv,toggle_rect_consec4]

	for toggle_button in toggle_buttons:
		pygame.draw.rect(window, gray, toggle_button['shape'])
		pygame.draw.rect(window, black, toggle_button['shape'], 2)

		text_surface = font.render(toggle_button['text'], True, black)
		text_rect = text_surface.get_rect(center=toggle_button['shape'].center)
		window.blit(text_surface, text_rect)

	run = True
	while run: 
		MENU_MOUSE_POS = pygame.mouse.get_pos()

		if play_button.draw(window):
			print('PLAY')
		
		# event handlers
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				run = False
				break
			if play_button.checkForInput(MENU_MOUSE_POS):
				game_screen()
			if event.type == pygame.MOUSEBUTTONDOWN:
				for toggle_button in toggle_buttons:
					if toggle_button['shape'].collidepoint(event.pos):
						toggle_button['state'] = not toggle_button['state']
						toggle_button['text'] = "Off" if toggle_button['state'] else "On"
						print(f'{toggle_button['rule']} {toggle_button['text']}')
						pygame.draw.rect(window, gray, toggle_button['shape'])
						pygame.draw.rect(window, black, toggle_button['shape'], 2)

						text_surface = font.render(toggle_button['text'], True, black)
						text_rect = text_surface.get_rect(center=toggle_button['shape'].center)
						window.blit(text_surface, text_rect)

						change_rule(toggle_button['rule'], toggle_button['state'])
		pygame.display.flip()
	pygame.quit()

def change_rule(rule_name, rule_state):
	game_rules.slapRules[rule_name] = rule_state

main_menu()
pygame.quit()
