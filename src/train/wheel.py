import pygame
from constants import *


class Wheel:
    def __init__(self):
        self.__axle = None
        self.__MAXIMUM_FORCE_TRANSFER_TO_RAIL = self.__get_maximum_force_transfer_to_rail()

        self.__is_skipping = False
        self.__wheelspeed = 0


    def draw(self):
        pass

    def get_acceleration_force(self, train_speed):
        axle_power = self.__axle.get_power()

        # At o velocity, acceleration force would be infinity for very small amount of time.
        if abs(train_speed) <= VERY_SMALL_SPEED:
            wheel_force = axle_power / VERY_SMALL_SPEED
        else:
            wheel_force = axle_power / abs(train_speed)
        self.__is_skipping = wheel_force > self.__MAXIMUM_FORCE_TRANSFER_TO_RAIL
        if not self.__is_skipping:
            return wheel_force
        return


    def __get_maximum_force_transfer_to_rail(self):
        #TODO
        pass