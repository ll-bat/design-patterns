from abc import ABC, abstractmethod


class Color:
    figure = None

    def __init__(self, figure):
        self.figure = figure

    @abstractmethod
    def print_color(self):
        pass

    @abstractmethod
    def set_color(self):
        pass


class Red(Color):
    def print_color(self):
        print('red')

    def set_color(self):
        self.figure.set_color('red')


class Blue(Color):
    def print_color(self):
        print('blue')

    def set_color(self):
        self.figure.set_color('blue')


class Figure(ABC):
    color: str = None

    @abstractmethod
    def set_color(self, color):
        pass

    def draw(x, y):
        pass


class Circle(Figure):
    def on_color_change(self, color):
        print("Circle color changed to: {}".format(color))

    def do_something1(self):
        pass

    def do_something2(self):
        pass

    def set_color(self, color):
        self.color = color
        self.on_color_change(color)
        self.do_something1()
        self.do_something2()


class Square(Figure):
    def on_color_change(self, color):
        print('Square color changed to: {}'.format(color))

    def do_different_thing1(self):
        pass

    def do_different_thing2(self):
        pass

    def set_color(self, color):
        self.color = color
        self.on_color_change(color)
        self.do_different_thing1()
        self.do_different_thing2()


class App:
    def init(self):
        circle = Circle()
        red_circle = Red(circle)
        red_circle.set_color()

        square = Square()
        blue_square = Blue(square)
        blue_square.set_color()


app = App()
app.init()
