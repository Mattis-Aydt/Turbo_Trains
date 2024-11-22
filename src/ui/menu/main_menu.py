import pygame

from ui.menu.menu import Menu
from ui.menu.menu_type import MenuType
from ui.button import Button


class MainMenu(Menu):
    def __init__(self, menu_type: MenuType, win, fps):
        super().__init__(menu_type, win, fps)
        self.__run = True
        play_button = Button("../resources/buttons/play/", self.win, (100, 100), (200, 200), action=self.switch_to_play)
        self.buttons.append(play_button)
        settings_button = Button("../resources/buttons/settings/", self.win, (100, 100), (200, 400), action=self.switch_to_settings)
        self.buttons.append(settings_button)
        self.background_color = (100, 100, 100)

    def switch_to_settings(self):
        self.next_menu_type = MenuType.SETTINGS
        self._run = False

    def switch_to_play(self):
        self.next_menu_type = MenuType.SIMULATION
        self._run = False

    def reset(self):
        self._run = True

