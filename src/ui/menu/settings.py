import pygame
from ui.menu.menu import Menu
from ui.menu.menu_type import MenuType
from ui.button import Button


class SettingsMenu(Menu):
    def __init__(self, menu_type: MenuType, win, fps):
        super().__init__(menu_type, win, fps)
        back_button = Button("../resources/buttons/back/", self.win, (100, 100), (600, 200), action=self.switch_to_main)
        self.buttons.append(back_button)

    def reset(self):
        self._run = True

    def switch_to_main(self):
        self.next_menu_type = MenuType.MAIN_MENU
        self._run = False


