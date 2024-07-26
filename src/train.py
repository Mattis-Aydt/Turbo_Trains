import pygame.draw
from map import Map
from railcar import Railcar

from ttMath import *
class Train:
    def __init__(self, map):
        self.__speed = 0
        self.__acceleration_input = 0
        self.map = map

        self.__railcars = [Railcar(self.map, 0), Railcar(self.map, 50), Railcar(self.map, 100), Railcar(self.map, 150), Railcar(self.map, 200)]

    def update(self):
        acceleration = 0
        for railcar in self.__railcars:
            acceleration += railcar.get_acceleration(self.__acceleration_input)
        self.__speed += acceleration

        for railcar in self.__railcars:
            railcar.set_speed(self.__speed)
            railcar.update()

    def draw(self, win, cam):
        for railcar in self.__railcars:
            railcar.draw(win, cam)

    def set_acceleration_input(self, value):
        self.__acceleration_input = value

