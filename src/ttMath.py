import math
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


def is_interval_overlapping(x1, x2, y1, y2):
    if x1 > y1:
        x1, y1 = y1, x1
        x2, y2 = y2, x2
    if y1 > x2:
        return False
    return True


def get_linear_approximation(splines, step_size=.1):
    points = []
    for spline in splines:
        amount_of_linears = int((spline["end"] - spline["start"]) / step_size) + 1
        starting_point = (spline["start"], evaluate_polinomial(spline["polinomial"], 0))
        for i in range(amount_of_linears):
            point = (starting_point[0] + i * step_size, evaluate_polinomial(spline["polinomial"], i * step_size))
            points.append(point)
    return points
def get_distance(p1, p2):
    return math.sqrt(pow(p1[0]-p2[0], 2) + pow(p1[1] - p2[1], 2))

