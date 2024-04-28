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

# fonts
fontHead = pygame.font.SysFont('comicsans', 60)
fontBody = pygame.font.SysFont('comicsans', 30)
font = pygame.font.SysFont('comicsans', 20)

pygame.display.set_caption("Rat Slapper")


# HOME SCREEN
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

		# draw buttons
		if play_button.draw(window):
			print('PLAY')
		if rules_button.draw(window):
			print('RULES')

		# event handler
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

# INSTRUCTIONS SCREEN
def show_instructions():
	window.fill((202, 228, 241))

	textHead = fontHead.render("Instructions", True, (255,255,255))
	textBody = fontBody.render("meow meow meow\n cows cows cows\n", True, (255,255,255))

	# load button 
	back_btn_img = pygame.image.load('images/backbtn.png').convert_alpha()

	# create button instances
	back_button = Button(100, 600, back_btn_img, 0.5)

	window.blit(textHead, (100, 100))

	textRules = ["1. CATS",
				"2. DOGS"]
	yValue = 200

	# print instructions
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

		# event handler	
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				run = False
				break
			if event.type == pygame.MOUSEBUTTONDOWN:
				if back_button.checkForInput(MENU_MOUSE_POS):
					main_menu()

		pygame.display.update()
	pygame.quit()
	
# CONFIGURATION SCREEN
def configuration_screen():
	window.fill((202, 228, 241))

	textHead = fontHead.render("Rule Modifications", True, (255,255,255))

	# load play button 
	play_img = pygame.image.load('images/play.png').convert_alpha()

	# create button instances
	play_button = Button(700, 500, play_img, 0.4)
	window.blit(textHead, (100, 50))

	# Toggle buttons
	toggle_rect_2InARow = {
		'shape': pygame.Rect(100, 200, 75, 30),
		'state': False,
		'text': 'On',
		'rule': '2InARow'
	}
	toggle_rect_sandwich = {
		'shape': pygame.Rect(100, 250, 75, 31),
		'state': False,
		'text': 'On',
		'rule': 'sandwich'
	}
	toggle_rect_addTo10 = {
		'shape': pygame.Rect(100, 300, 75, 32),
		'state': False,
		'text': 'On',
		'rule': 'addTo10'
	}		
	toggle_rect_sandwich10 = {
		'shape': pygame.Rect(100, 350, 75, 33),
		'state': False,
		'text': 'On',
		'rule': 'sandwich10'
	}
	toggle_rect_marriage = {
		'shape': pygame.Rect(100, 400, 75, 34),
		'state': False,
		'text': 'On',
		'rule': 'marriage'
	}
	toggle_rect_divorce = {
		'shape': pygame.Rect(100, 450, 75, 35),
		'state': False,
		'text': 'On',
		'rule': 'divorce'
	}
	toggle_rect_topBottom = {
		'shape': pygame.Rect(100, 500, 75, 36),
		'state': False,
		'text': 'On',
		'rule': 'topBottom'
	}
	toggle_rect_topBottomAdd = {
		'shape': pygame.Rect(100, 550, 75, 37),
		'state': False,
		'text': 'On',
		'ruke': 'topBottomAdd'
	}
	toggle_rect_topBottomDiv = {
		'shape': pygame.Rect(100, 600, 75, 38),
		'state': False,
		'text': 'On',
		'rule': 'topBottomDiv'
	}
	toggle_rect_consec4 = {
		'shape': pygame.Rect(100, 650, 75, 39),
		'state': False,
		'text': 'On',
		'rule': 'consec4'
	}

	toggle_buttons = [toggle_rect_2InARow, toggle_rect_sandwich, 
			toggle_rect_addTo10, toggle_rect_sandwich10, 
			toggle_rect_marriage, toggle_rect_divorce,
			toggle_rect_topBottom, toggle_rect_topBottomAdd, 
			toggle_rect_topBottomDiv,toggle_rect_consec4]

	# Display Toggles
	for toggle_button in toggle_buttons:
		pygame.draw.rect(window, gray, toggle_button['shape'])
		pygame.draw.rect(window, black, toggle_button['shape'], 2)

		text_surface = font.render(toggle_button['text'], True, black)
		text_rect = text_surface.get_rect(center=toggle_button['shape'].center)
		window.blit(text_surface, text_rect)

	# Toggle Labels 
	text_rule_2InARow = font.render("      In a Row", True, (255,255,255))
	text_rule_sandwich = font.render("Sandwhich", True, (255,255,255))
	text_rule_addTo10 = font.render("Add to       ", True, (255,255,255))
	text_rule_sandwich10= font.render("Sandwhich       ", True, (255,255,255))
	text_rule_marriage = font.render("Marriage", True, (255,255,255))
	text_rule_divorce = font.render("Divorce", True, (255,255,255))
	text_rule_topBottom = font.render("Top Bottolm", True, (255,255,255))
	text_rule_topBottomAdd = font.render("Top Bottom Add", True, (255,255,255))
	text_rule_topBottomDiv = font.render("Top Bottom Div", True, (255,255,255))
	text_rule_consec4 = font.render("Consecutive 4", True, (255,255,255))

	toggle_labels = [text_rule_2InARow , text_rule_sandwich, 
			text_rule_addTo10, text_rule_sandwich10, 
			text_rule_marriage, text_rule_divorce,
			text_rule_topBottom, text_rule_topBottomAdd, 
			text_rule_topBottomDiv,text_rule_consec4]
	
	# Display Toggle Labels
	toggle_value_y = 200
	for toggle_label in toggle_labels:
		window.blit(toggle_label, (200, toggle_value_y))
		toggle_value_y += 50
 
	###  ____ IN A ROW VALUE CHANGER ###
	num_in_a_row = 1
	# Draw number selector box
	selector_box_1 = pygame.Rect(200, 200, 30, 30)
	pygame.draw.rect(window, white, selector_box_1)
	pygame.draw.rect(window, black, selector_box_1, 2)

	# Draw selected number
	text_surface = font.render(str(num_in_a_row), True, black)
	text_rect = text_surface.get_rect(center=selector_box_1.center)
	window.blit(text_surface, text_rect)

	# Draw up and down arrows
	down_arrow_rect = pygame.Rect(203, 235, 20, 10)
	up_arrow_rect = pygame.Rect(203, 185, 20, 10)
	pygame.draw.polygon(window, black, [(up_arrow_rect.centerx, up_arrow_rect.top),
										(up_arrow_rect.left + 5, up_arrow_rect.bottom),
										(up_arrow_rect.right - 5, up_arrow_rect.bottom)])
	
	pygame.draw.polygon(window, black, [(down_arrow_rect.centerx, down_arrow_rect.bottom),
										(down_arrow_rect.left + 5, down_arrow_rect.top),
										(down_arrow_rect.right - 5, down_arrow_rect.top)])
	
	### ADD TO ___ CHANGER ###
	add_to_num = 1
	# Draw number selector box
	selector_box_2 = pygame.Rect(275, 300, 30, 30)
	pygame.draw.rect(window, white, selector_box_2)
	pygame.draw.rect(window, black, selector_box_2, 2)

	# Draw selected number
	text_surface = font.render(str(num_in_a_row), True, black)
	text_rect = text_surface.get_rect(center=selector_box_2.center)
	window.blit(text_surface, text_rect)

	# Draw up and down arrows
	down_arrow_rect_2 = pygame.Rect(278, 335, 20, 10)
	up_arrow_rect_2 = pygame.Rect(278, 285, 20, 10)
	pygame.draw.polygon(window, black, [(up_arrow_rect_2.centerx, up_arrow_rect_2.top),
										(up_arrow_rect_2.left + 5, up_arrow_rect_2.bottom),
										(up_arrow_rect_2.right - 5, up_arrow_rect_2.bottom)])
	
	pygame.draw.polygon(window, black, [(down_arrow_rect_2.centerx, down_arrow_rect_2.bottom),
										(down_arrow_rect_2.left + 5, down_arrow_rect_2.top),
										(down_arrow_rect_2.right - 5, down_arrow_rect_2.top)])
	

	### SANDWICH ___ ###
	sandwich_num = 1
	# Draw number selector box
	selector_box_3 = pygame.Rect(310, 350, 30, 30)
	pygame.draw.rect(window, white, selector_box_3)
	pygame.draw.rect(window, black, selector_box_3, 2)

	# Draw selected number
	text_surface = font.render(str(num_in_a_row), True, black)
	text_rect = text_surface.get_rect(center=selector_box_3.center)
	window.blit(text_surface, text_rect)

	# Draw up and down arrows
	down_arrow_rect_3 = pygame.Rect(313, 385, 20, 10)
	up_arrow_rect_3 = pygame.Rect(313, 335, 20, 10)
	pygame.draw.polygon(window, black, [(up_arrow_rect_3.centerx, up_arrow_rect_3.top),
										(up_arrow_rect_3.left + 5, up_arrow_rect_3.bottom),
										(up_arrow_rect_3.right - 5, up_arrow_rect_3.bottom)])
	
	pygame.draw.polygon(window, black, [(down_arrow_rect_3.centerx, down_arrow_rect_3.bottom),
										(down_arrow_rect_3.left + 5, down_arrow_rect_3.top),
										(down_arrow_rect_3.right - 5, down_arrow_rect_3.top)])
	
	### CONSECUTIVE ___ ###
	consecutive_num = 1
	# Draw number selector box
	selector_box_4 = pygame.Rect(315, 650, 30, 30)
	pygame.draw.rect(window, white, selector_box_4)
	pygame.draw.rect(window, black, selector_box_4, 2)

	# Draw selected number
	text_surface = font.render(str(num_in_a_row), True, black)
	text_rect = text_surface.get_rect(center=selector_box_4.center)
	window.blit(text_surface, text_rect)

	# Draw up and down arrows
	down_arrow_rect_4 = pygame.Rect(320, 685, 20, 10)
	up_arrow_rect_4 = pygame.Rect(320, 635, 20, 10)
	pygame.draw.polygon(window, black, [(up_arrow_rect_4.centerx, up_arrow_rect_4.top),
										(up_arrow_rect_4.left + 5, up_arrow_rect_4.bottom),
										(up_arrow_rect_4.right - 5, up_arrow_rect_4.bottom)])
	
	pygame.draw.polygon(window, black, [(down_arrow_rect_4.centerx, down_arrow_rect_4.bottom),
										(down_arrow_rect_4.left + 5, down_arrow_rect_4.top),
										(down_arrow_rect_4.right - 5, down_arrow_rect_4.top)])

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
			elif event.type == pygame.MOUSEBUTTONDOWN:
				for toggle_button in toggle_buttons:
					# Update toggle state if clicked
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
				if event.button == 1: 
					### ___ IN A ROW ###
					# Check if the click is within the up or down arrow
					if up_arrow_rect.collidepoint(event.pos):
						if num_in_a_row < 10:
							num_in_a_row += 1
						print(num_in_a_row, 'in a row')
					elif down_arrow_rect.collidepoint(event.pos):
						if num_in_a_row > 1 : 
							num_in_a_row -= 1
						print(num_in_a_row, 'in a row')
					# Draw selected number
					pygame.draw.rect(window, white, selector_box_1)
					pygame.draw.rect(window, black, selector_box_1, 2)
					text_surface = font.render(str(num_in_a_row), True, black)
					text_rect = text_surface.get_rect(center=selector_box_1.center)
					window.blit(text_surface, text_rect)

					### ADD TO ___ ###
					# Check if the click is within the up or down arrow
					if up_arrow_rect_2.collidepoint(event.pos):
						if add_to_num < 10:
							add_to_num += 1
						print('add to num', add_to_num)
					elif down_arrow_rect_2.collidepoint(event.pos):
						if add_to_num > 1 : 
							add_to_num -= 1
						print('add to num', add_to_num)
					# Draw selected number
					pygame.draw.rect(window, white, selector_box_2)
					pygame.draw.rect(window, black, selector_box_2, 2)
					text_surface = font.render(str(add_to_num), True, black)
					text_rect = text_surface.get_rect(center=selector_box_2.center)
					window.blit(text_surface, text_rect)

					### SANDWICH ___ ###
					# Check if the click is within the up or down arrow
					if up_arrow_rect_3.collidepoint(event.pos):
						if sandwich_num < 10:
							sandwich_num += 1
						print('sandwich', sandwich_num)
					elif down_arrow_rect_3.collidepoint(event.pos):
						if sandwich_num > 1 : 
							sandwich_num -= 1
						print('sandwich', sandwich_num)
					# Draw selected number
					pygame.draw.rect(window, white, selector_box_3)
					pygame.draw.rect(window, black, selector_box_3, 2)
					text_surface = font.render(str(sandwich_num), True, black)
					text_rect = text_surface.get_rect(center=selector_box_3.center)
					window.blit(text_surface, text_rect)

					### CONSECUTIVE ___ ###
					# Check if the click is within the up or down arrow
					if up_arrow_rect_4.collidepoint(event.pos):
						if consecutive_num < 10:
							consecutive_num += 1
						print('consecutive', consecutive_num)
					elif down_arrow_rect_3.collidepoint(event.pos):
						if consecutive_num > 1 : 
							consecutive_num -= 1
						print('consecutive', consecutive_num)
					# Draw selected number
					pygame.draw.rect(window, white, selector_box_4)
					pygame.draw.rect(window, black, selector_box_4, 2)
					text_surface = font.render(str(consecutive_num), True, black)
					text_rect = text_surface.get_rect(center=selector_box_4.center)
					window.blit(text_surface, text_rect)

		pygame.display.flip()
	pygame.quit()

def change_rule(rule_name, rule_state):
	game_rules.slapRules[rule_name] = rule_state
	
main_menu()
