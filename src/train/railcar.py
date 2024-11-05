from ttMath import *
import pygame
from constants import *
class Railcar:
    def __init__(self, map, x):
        self.__x = x
        self.__speed = 0
        self.__power = 800000
        self.__mass = 45000
        self.map = map
        self.length = 50
        self.height = 2
        self.wheels = []

    def draw(self, win, cam):

        pos = (self.__x, self.map.get_y(self.__x))
        pos_in_pixels = cam.transform_point_to_pixels(pos)
        size = cam.scale((self.length, self.height))
        pygame.draw.rect(win, (0, 100, 200), (pos_in_pixels[0], pos_in_pixels[1], size[0], size[1]))

    def update(self, time_delta):
        self.move(time_delta)

    def set_speed(self, value):
        self.__speed = value

    def move(self, time_delta):
        relevant_splines = self.map.get_section(self.__x, self.__x)
        points = get_linear_approximation(relevant_splines)
        current_point_index = None
        for i in range(len(points)-1):
            if is_interval_overlapping(self.__x, self.__x, points[i][0], points[i+1][0]):
                current_point_index = i
                break
        if current_point_index is None:
            raise RuntimeError("current_point_index needs to be set in order for move to work")

        relevant_points = points[current_point_index:]
        relevant_points[0] = (self.__x, self.map.get_y(self.__x))

        traveling_distance = self.__speed*time_delta
        i = 0
        while traveling_distance - get_distance(relevant_points[i], relevant_points[i+1]) >= 0:
            traveling_distance -= get_distance(relevant_points[i], relevant_points[i + 1])
            i += 1

        if get_distance(relevant_points[i], relevant_points[i+1]) == 0:
           relevant_points = relevant_points[1:]

        left_over_speed_on_last_linear = traveling_distance / get_distance(relevant_points[i], relevant_points[i+1])
        x_length_of_last_linear = relevant_points[i+1][0] - relevant_points[i][0]
        new_x = left_over_speed_on_last_linear * x_length_of_last_linear + relevant_points[i][0]
        self.__x = new_x

    def get_acceleration_force(self, power_input):
        gradient = self.map.get_gradient(self.__x)
        g_force = gradient/(abs(gradient)+1) * G * self.__mass

        # At o velocity, acceleration force would be infinity for very small amount of time.
        if abs(self.__speed) <= VERY_SMALL_SPEED:
            acceleration_force = (self.__power*power_input) / VERY_SMALL_SPEED
        else:
            acceleration_force = (self.__power*power_input) / abs(self.__speed)

        total_force = acceleration_force - g_force

        return total_force

    def get_mass(self):
        return self.__mass
