import pygame

from src.ui.menu.menu import Menu
from ui.menu.menu_type import MenuType
from ui.button import Button


class MainMenu(Menu):
    def __init__(self, menu_type: MenuType, win):
        super().__init__(menu_type, win)
        self.backbutton = Button("C:/Users/matti/Dev/AdvancedProjects/Turbo_Trains/resources/buttons/button1", self.win, (100, 100), (100, 100))

    def reset(self):
        pass

    def run(self):
        run = True
        while run:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False

            self.win.fill((200, 200, 200))
            self.backbutton.draw()
            pygame.display.update()
