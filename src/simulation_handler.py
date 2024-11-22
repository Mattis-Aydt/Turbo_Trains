from ui.drawable import Drawable
from map import Map
from camera import Camera


class SimulationHandler:
    def __init__(self, win, map_name):
        self.drawables: list[Drawable] = []
        self.cam = Camera(win.get_size())
        self.map = Map(win, self.cam)
        self.map.load_data("../resources/", map_name)
        self.drawables.append(self.map)
