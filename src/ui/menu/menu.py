import pygame
from abc import ABC, abstractmethod
from src.ui.menu.menu_type import MenuType


class Menu(ABC):
    def __init__(self, menu_type: MenuType, win):
        self.win = win
        self.menu_type = menu_type
        self.next_menu_type = MenuType.OFF

    @abstractmethod
    def reset(self):
        pass

    def get_next_menu_type(self):
        return self.next_menu_type

    @abstractmethod
    def run(self):
        pass
