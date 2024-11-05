import pygame


class Button:
    def __init__(self, template_path, win, size, pos):
        self.win = win
        self.pos = pos
        self.sound_click = None
        self.sound_hover = None
        self.img_down = None
        self.img_up = None
        self.load(template_path)
        if self.img_up:
            pygame.transform.scale(self.img_up, size)
        if self.img_down:
            pygame.transform.scale(self.img_down, size)

    def load(self, template_path):
        try:
            self.img_up = pygame.image.load(template_path + "/button_img_up.png").convert_alpha()
        except ValueError:
            raise FileNotFoundError("Path is incorrect or doesnt contain necessary files")
        try:
            self.img_down = pygame.image.load(template_path + "/button_img_down.png").convert_alpha()
            self.sound_hover = pygame.mixer.Sound(template_path + "/button_sound_hover.mp3")
            self.sound_click = pygame.mixer.Sound(template_path + "/button_sound_click.mp3")
        except FileNotFoundError:
            pass

    def draw(self):
        self.win.blit(self.img_up, self.pos)

