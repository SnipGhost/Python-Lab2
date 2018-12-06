from lab_python_oop.Figure import Figure
from lab_python_oop.Color import Color


class Rectangle(Figure):

    def __init__(self, width, height, colour):
        self.__area = 0
        self.__width = 0
        self.__height = 0
        self.width = width
        self.height = height
        self.color = Color(colour)
        super(Rectangle, self).__init__('Прямоугольник')

    @property
    def area(self):
        return self.__area

    def calc_area(self):
        return self.__width * self.__height

    def width_get(self):
        return self.__width

    def width_set(self, val):
        self.__width = val
        self.__area = self.calc_area()

    def height_get(self):
        return self.__height

    def height_set(self, val):
        self.__height = val
        self.__area = self.calc_area()

    def __repr__(self):
        tpl = '{}:\n\tЦвет: {}\n\tШирина: {}\n\tВысота: {}\n\tПлощадь: {}\n'
        return tpl.format(self.name, self.color, self.width, self.height, self.area)

    width = property(width_get, width_set, None, 'Width')
    height = property(height_get, height_set, None, 'Height')
