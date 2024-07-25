import pygame.draw
from map import Map

from ttMath import *
class Train:
    def __init__(self, map):
        self.__x = .5
        self.__speed = .1
        self.map = map

    def update(self):
        self.move()

    def draw(self, win, cam, map):
        pos = (self.__x, map.get_y(self.__x))
        pos_in_pixels = cam.transform_point_to_pixels(pos)
        pygame.draw.circle(win, (0, 100, 200), pos_in_pixels, 10)

    def move(self):
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

        speed = self.__speed
        i = 0
        while speed - get_distance(relevant_points[i], relevant_points[i+1]) > 0:
            speed -= get_distance(relevant_points[i], relevant_points[i + 1])
            i += 1

        left_over_speed_on_last_linear = speed / get_distance(relevant_points[i], relevant_points[i+1])
        x_length_of_last_linear = relevant_points[i+1][0] - relevant_points[i][0]
        new_x = left_over_speed_on_last_linear * x_length_of_last_linear + relevant_points[i][0]
        self.__x = new_x

    def move_bad(self):
        self.__x += self.__speed

        

