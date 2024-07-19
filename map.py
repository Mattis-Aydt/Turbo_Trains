import pygame.draw
import json


class Map:
    def __init__(self):
        self.data = {}

    def load_data(self, ressources_path, map_name):
        with open(ressources_path + map_name, "r") as f:
            self.data = json.load(f)
            print(self.data)
        #self.check_splines()

    # Check wether the splines have same derivatives at end and starting point
    def check_splines(self):
        end_derivative = 0
        for spline in self.data["splines"]:
            derivative = get_polinomial_derivative(spline[:-1])
            start_derivative = evaluate_polinomial(derivative, 0)
            if end_derivative != start_derivative:
                raise RuntimeError("Map Data seems to be incorrect. Derivatives dont match at spline " + str(spline))
            if spline[0] != 0:
                raise RuntimeError(
                    "Map Data seems to be incorrect. Spline needs to start at height 0. At spline  " + str(spline))
            end_derivative = evaluate_polinomial(derivative, spline[-1])

    def draw(self, win, cam):
        for spline in self.data["splines"]:
            draw_spline(win, cam, spline, 0.1)


def draw_spline(win, cam, spline, step_size):
    polinomial_length = int((spline[-1] - spline[-2]) / step_size) + 1
    polinomial = spline[:-2]
    starting_point = (spline[-2], evaluate_polinomial(polinomial, 0))
    prev_point = (starting_point[0] - cam.get_x(), starting_point[1] - cam.get_y())
    for x in range(polinomial_length):
        x = x * step_size
        y = evaluate_polinomial(polinomial, x)
        point = (x + starting_point[0] - cam.get_x(), y - cam.get_y())
        pygame.draw.line(win, (255, 0, 0), cam.transform_point_to_pixels(prev_point),
                         cam.transform_point_to_pixels(point), 2)
        prev_point = point


def evaluate_polinomial(polinomial, x, ):
    result = 0
    for i in range(len(polinomial)):
        result += polinomial[i] * pow(x, i)
    return result


def get_polinomial_derivative(polinomial):
    if not polinomial:
        return []

    derivative = []
    for i in range(len(polinomial)):
        derivative.append(i * polinomial[i])
    return derivative[1:]
