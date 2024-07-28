from ttMath import *
class Camera:
    def __init__(self, win_size):
        self.__x = 0
        self.__y = 0


        self.__zoom_x = 0.01
        self.__zoom_y = 0.01

        self.__win_size = win_size

        self.__focus_train = False
        self.__train = None

    def update(self):
        if self.__focus_train:
            x, y = self.__train.get_pos()
            self.__x = x
            self.__y = y
    def get_x(self):
        return self.__x

    def get_y(self):
        return self.__y

    def get_zoom_x(self):
        return self.__zoom_x

    def get_zoom_y(self):
        return self.__zoom_y

    def transform_meters_to_pixels(self, point):
        result = (point[0] - self.__x)/self.__zoom_x + self.__win_size[0]*.5, -(point[1] - self.__y)/self.__zoom_y + self.__win_size[1]*.5
        return result

    def scale(self, point):
        result = point[0]/self.__zoom_x, point[1]/self.__zoom_y
        return result

    def transform_pixels_to_meters(self):
        pass

    def move_x(self, amount):
        self.__x += amount*self.__zoom_x

    def move_y(self, amount):
        self.__y += amount*self.__zoom_y

    def zoom(self, amount):
        self.__zoom_x = self.__zoom_x - amount*self.__zoom_x
        self.__zoom_y = self.__zoom_y - amount * self.__zoom_y

    def focus_train(self, train):
        self.__train = train
        self.__focus_train = True

    def is_point_in_win(self, point):
        # TODO
        pass

    def is_interval_in_win(self, x1, x2, x_achsis_interval=True):
        y1, y2 = 0, self.__win_size[0]

        if not x_achsis_interval:
            y2 = self.__win_size[1]

        if x_achsis_interval:
            x1_as_pixels = self.transform_meters_to_pixels((x1, 0))[0]
            x2_as_pixels = self.transform_meters_to_pixels((x2, 0))[0]
        else:
            x1_as_pixels = self.transform_meters_to_pixels((0, x1))[1]
            x2_as_pixels = self.transform_meters_to_pixels((0, x2))[1]

        if x1_as_pixels > x2_as_pixels:
            x1_as_pixels, x2_as_pixels = x2_as_pixels, x1_as_pixels

        return is_interval_overlapping(x1_as_pixels, x2_as_pixels, y1, y2)

    def is_box_in_win(self):
        pass
