import pygame


class Button:
    def __init__(self, template_path, win, size, pos, action=None):
        self.win = win
        self.pos = pos
        self.size = size
        self.action = action
        self.sound_click = None
        self.sound_hover = None
        self.img_down = None
        self.img_up = None
        self.load(template_path)

        self.mouse_hovers = False

    def load(self, template_path):
        try:
            self.img_up = pygame.image.load(template_path + "button_img_up.png").convert_alpha()
            self.img_up = pygame.transform.scale(self.img_up, self.size)
        except ValueError:
            raise FileNotFoundError("Path is incorrect or doesnt contain necessary files")
        try:
            self.img_down = pygame.image.load(template_path + "button_img_down.png").convert_alpha()
            self.img_down = pygame.transform.scale(self.img_down, self.size)

            self.sound_hover = pygame.mixer.Sound(template_path + "button_sound_hover.mp3")
            self.sound_click = pygame.mixer.Sound(template_path + "button_sound_click.mp3")
        except FileNotFoundError:
            pass

    def draw(self):
        if self.mouse_hovers and self.img_down:
            self.win.blit(self.img_down, self.pos)
        else:
            self.win.blit(self.img_up, self.pos)

    def update(self, mouse_pos, mouse_clicked):
        self.mouse_hovers = self.pos[0] < mouse_pos[0] < self.pos[0] + self.size[0] and self.pos[1] < mouse_pos[1] < self.pos[1] + self.size[1]
        if mouse_clicked and self.mouse_hovers:
            self.action()



