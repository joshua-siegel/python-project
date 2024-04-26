import pygame
from models import *
from game import * 

pygame.init()

screen_height = 768
screen_width = 1024
bounds = (screen_width, screen_height)
window = pygame.display.set_mode(bounds)
pygame.display.set_caption("Rat Slapper")