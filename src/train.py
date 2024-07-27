import pygame.draw
from map import Map
from railcar import Railcar
import time

from ttMath import *
class Train:
    def __init__(self, map):
        self.__speed = 0/3.6
        self.__acceleration_input = 0
        self.map = map
        self.speed_timer = None

        self.__railcars = [Railcar(self.map, 0)]

    def update(self, time_delta):
        accelerations = []
        for railcar in self.__railcars:
            accelerations.append(railcar.get_acceleration(self.__acceleration_input))
        acceleration = sum(accelerations)/len(accelerations)
        self.__speed += acceleration*time_delta

        for railcar in self.__railcars:
            railcar.set_speed(self.__speed)
            railcar.update(time_delta)

    def draw(self, win, cam):
        for railcar in self.__railcars:
            railcar.draw(win, cam)

    def set_acceleration_input(self, value):
        if not self.speed_timer and value == 1:
            self.speed_timer = time.time()
        self.__acceleration_input = value

