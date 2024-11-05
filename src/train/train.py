import pygame.draw
from map import Map
from src.train.railcar import Railcar
import time
from constants import *

from ttMath import *
class Train:
    def __init__(self, map):
        self.__speed = 0/3.6
        self.__acceleration_input = 0
        self.map = map

        self.cw_times_A = .51

        self.__railcars = [Railcar(self.map, 0)]

    def update(self, time_delta):
        acceleration_forces = []
        masses = []
        for railcar in self.__railcars:
            acceleration_forces.append(railcar.get_acceleration_force(self.__acceleration_input))
            masses.append(railcar.get_mass())
        acceleration_force = sum(acceleration_forces)
        ground_resistance_force = 0
        air_resistance_force = self.get_air_resistance_force()
        mass = sum(masses)

        total_force = acceleration_force - air_resistance_force - ground_resistance_force
        acceleration = total_force / mass
        print(self.__speed*3.6)
        self.__speed += acceleration*time_delta

        for railcar in self.__railcars:
            railcar.set_speed(self.__speed)
            railcar.update(time_delta)

    def draw(self, win, cam):
        for railcar in self.__railcars:
            railcar.draw(win, cam)

    def set_acceleration_input(self, value):
        self.__acceleration_input = value

    def get_air_resistance_force(self):
        return 0.5 * P * pow(self.__speed, 2) * self.cw_times_A
