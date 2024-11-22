import pygame

from ui.menu.menu_handler import MenuHandler
from simulation_handler import SimulationHandler

pygame.init()
win = pygame.display.set_mode((1000, 1000))

menu_handler = MenuHandler(win, 60)
menu_handler.start()