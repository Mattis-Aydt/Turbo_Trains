import pygame
from src import camera
import map

def draw(win, cam, map):
    win.fill((255, 255, 255))
    map.draw(win, cam)

    pygame.display.update()


framerate = 60
pygame.init()
clock = pygame.time.Clock()
win = pygame.display.set_mode((1000, 1000))
cam = camera.Camera((1000, 1000))
map = map.Map()
map.load_data("../ressources/", "test_map.json")

run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                pass
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 4:
                cam.zoom(0.1)
            elif event.button == 5:
                cam.zoom(-0.1)

    keys = pygame.key.get_pressed()
    if keys[pygame.K_a]:
        cam.move_x(-1000/framerate)
    if keys[pygame.K_d]:
        cam.move_x(1000/framerate)
    if keys[pygame.K_w]:
        cam.move_y(1000/framerate)
    if keys[pygame.K_s]:
        cam.move_y(-1000/framerate)


    clock.tick(framerate)
    cam.update()


    draw(win, cam, map)
