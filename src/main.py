import pygame

from ui.menu.menu_handler import MenuHandler

pygame.init()
win = pygame.display.set_mode((1000, 1000))


menu_handler = MenuHandler(win)
menu_handler.start()