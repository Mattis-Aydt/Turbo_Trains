import pygame
from abc import ABC, abstractmethod
from ui.menu.menu_type import MenuType


class Menu(ABC):
    def __init__(self, menu_type: MenuType, win, fps):
        self.clock = pygame.time.Clock()
        self.win = win
        self.fps = fps
        self.menu_type = menu_type
        self.next_menu_type = MenuType.OFF
        self._run = True
        self.buttons = []
        self.background_color = (200, 200, 200)
        self.background = None

    @abstractmethod
    def reset(self):
        pass

    def get_next_menu_type(self):
        return self.next_menu_type

    def run(self):
        while self._run:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self._run = False
                    self.next_menu_type = MenuType.OFF
            mouse_pos = pygame.mouse.get_pos()
            mouse_button_clicked = pygame.mouse.get_pressed()

            self.win.fill(self.background_color)
            if self.background:
                self.win.blit(self.background, (0, 0))
            for button in self.buttons:
                button.update(mouse_pos, mouse_button_clicked[0])
                button.draw()
            pygame.display.update()
            self.clock.tick(self.fps)


