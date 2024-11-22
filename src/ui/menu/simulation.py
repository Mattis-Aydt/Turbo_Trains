import pygame
from ui.menu.menu import Menu
from ui.menu.menu_type import MenuType
from ui.button import Button
import map
import camera


class SimulationMenu(Menu):
    def __init__(self, menu_type: MenuType, win, fps):
        super().__init__(menu_type, win, fps)
        self.simulation_handler = None
        self.background_color = (50, 200, 30)

    def reset(self):
        self._run = True

    def run(self):
        if not self.simulation_handler:
            raise AttributeError("To be able to run a simulation handler has to be set")
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

            for drawable in self.simulation_handler.drawables:
                drawable.draw()

            for button in self.buttons:
                button.update(mouse_pos, mouse_button_clicked[0])
                button.draw()

            pygame.display.update()
            self.clock.tick(self.fps)

    def set_simulation_handler(self, simulation_handler):
        self.simulation_handler = simulation_handler
