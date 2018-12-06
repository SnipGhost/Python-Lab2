from lab_python_oop.Figure import Figure
from lab_python_oop.Color import Color


class Circle(Figure):

    # Add math package to requirements only for PI value? No, thanks!
    PI_VALUE = 3.14159265359

    def __init__(self, radius, color):
        self.__radius = 0
        self.__area = 0
        self.radius = radius
        self.radius_set(radius)
        self.color = Color(color)
        super(Circle, self).__init__('Круг')

    @property
    def area(self):
        return self.__area

    def radius_set(self, r):
        self.__radius = r
        self.__area = self.PI_VALUE * r * r

    def radius_get(self):
        return self.__radius

    def radius_del(self):
        del self.__radius

    def __repr__(self):
        tpl = '{}:\n\tЦвет: {}\n\tРадиус: {}\n\tПлощадь: {}\n'
        return tpl.format(self.name, self.color, self.radius, self.area)

    radius = property(radius_get, radius_set, radius_del, 'Radius')
