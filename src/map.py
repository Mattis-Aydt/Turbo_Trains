import pygame.draw
import json
from ttMath import *


class Map:
    def __init__(self):
        self.data = {}

        self.__prev_used_spline_index = 0

    def load_data(self, ressources_path, map_name):
        with open(ressources_path + map_name, "r") as f:
            self.data = json.load(f)
            for i in range(len(self.data["splines"])):
                self.data["splines"][i]["id"] = i

        #self.check_splines()

    # Check wether the splines have same derivatives at end and starting point
    def check_splines(self):
        end_derivative = 0
        for spline in self.data["splines"]:
            derivative = get_polinomial_derivative(spline["polinomial"])
            start_derivative = evaluate_polinomial(derivative, 0)
            if end_derivative != start_derivative:
                raise RuntimeError("Map Data seems to be incorrect. Derivatives dont match at spline " + str(spline))
            if spline[0] != 0:
                raise RuntimeError(
                    "Map Data seems to be incorrect. Spline needs to start at height 0. At spline  " + str(spline))
            end_derivative = evaluate_polinomial(derivative, spline[-1])

    def draw(self, win, cam):
        for spline in self.data["splines"]:
            if cam.is_interval_in_win(spline["start"], spline["end"]):
                draw_spline(win, cam, spline, math.sqrt(cam.get_zoom_x()*10))

    def get_section(self, start, finnish, lookahead=1, lookbehind=1):
        # Should be optimised with binary-search of section

        # Get splines in section
        splines = self.data["splines"]
        relevant_splines = []
        for spline in splines:
            if is_interval_overlapping(start, finnish, spline["start"], spline["end"]):
                relevant_splines.append(spline)
        first_index = relevant_splines[0]["id"]
        last_index = relevant_splines[-1]["id"]

        for i in range(lookahead):
            try:
                relevant_splines.append(self.data["splines"][last_index + 1 + i])
            except IndexError:
                pass
        for i in range(lookbehind):
            index = first_index - i - 1
            if index < 0:
                break
            relevant_splines.insert(0, self.data["splines"][index])
        return relevant_splines

    def get_spline(self, x):
        splines = self.data["splines"]
        i = self.__prev_used_spline_index
        j = self.__prev_used_spline_index
        while i < len(splines) and j >= 0:
            if is_interval_overlapping(x, x, splines[i]["start"], splines[i]["end"]):
                self.__prev_used_spline_index = i
                return splines[i]
            if is_interval_overlapping(x, x, splines[j]["start"], splines[j]["end"]):
                self.__prev_used_spline_index = j
                return splines[j]
            i += 1
            j -= 1

        if j < 0:
            while i < len(splines):
                if is_interval_overlapping(x, x, splines[i]["start"], splines[i]["end"]):
                    self.__prev_used_spline_index = i
                    return splines[i]
                i += 1
        else:
            while j >= 0:
                if is_interval_overlapping(x, x, splines[j]["start"], splines[j]["end"]):
                    self.__prev_used_spline_index = j
                    return splines[j]
                j -= 1
    def get_y(self, x):
        spline = self.get_spline(x)
        return evaluate_polinomial(spline["polinomial"], x-spline["start"])

    def get_gradient(self, x):
        spline = self.get_spline(x)
        return evaluate_polinomial(get_polinomial_derivative(spline["polinomial"]), x-spline["start"])













def draw_spline(win, cam, spline, step_size):
    print(step_size)
    polinomial_length = int((spline["end"] - spline["start"]) / step_size) + 1
    starting_point = (spline["start"], evaluate_polinomial(spline["polinomial"], 0))
    prev_point = (starting_point[0], starting_point[1])
    for x in range(polinomial_length):
        x = x * step_size
        y = evaluate_polinomial(spline["polinomial"], x)
        point = (x + starting_point[0], y)
        pygame.draw.line(win, (255, 0, 0), cam.transform_meters_to_pixels(prev_point),
                         cam.transform_meters_to_pixels(point), 2)
        prev_point = point




