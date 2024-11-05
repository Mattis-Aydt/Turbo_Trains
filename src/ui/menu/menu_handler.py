from ui.menu.main_menu import MainMenu
from ui.menu.settings import SettingsMenu
from ui.menu.menu_type import MenuType


class MenuHandler:
    def __init__(self, win):

        self.__main_menu = MainMenu(MenuType.MAIN_MENU, win)
        self.__settings_menu = SettingsMenu(MenuType.SETTINGS, win)

        self.__current_menu = self.__main_menu

    def start(self):
        while self.__current_menu:
            current_menu = self.__current_menu
            current_menu.run()
            next_menu_type = current_menu.get_next_menu_type()
            current_menu.reset()
            self.__current_menu = self.__get_menu_from_type(next_menu_type)

    def __get_menu_from_type(self, menu_type):
        if menu_type == MenuType.OFF:
            return None
        if menu_type == MenuType.MAIN_MENU:
            return self.__main_menu
        if menu_type == MenuType.SETTINGS:
            return self.__settings_menu
