from abc import ABC, abstractmethod
from ui.menu.menu_type import MenuType


class Drawable(ABC):
    def __init__(self):
        pass

    @abstractmethod
    def draw(self):
        pass
