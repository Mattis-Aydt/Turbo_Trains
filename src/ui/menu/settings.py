import pygame
from src.ui.menu.menu import Menu
from src.ui.menu.menu_type import MenuType


class SettingsMenu(Menu):
    def __init__(self, menu_type: MenuType):
        super().__init__(menu_type)

    def reset(self):
        pass

    def run(self):
        print("Settings menu")
        self.next_menu_type = MenuType.OFF