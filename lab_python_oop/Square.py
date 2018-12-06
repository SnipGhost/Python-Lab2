from lab_python_oop.Rectangle import Rectangle
from lab_python_oop.Color import Color


class Square(Rectangle):

    def __init__(self, length, color):
        super(Square, self).__init__(length, length, color)
        self.name = 'Квадрат'

    # Explicit is better than implicit (Zen of Python, 2)
    def length_set(self, val):
        self._Rectangle__width = val
        self._Rectangle__height = val
        self._Rectangle__area = super(Square, self).calc_area()

    def __repr__(self):
        tpl = '{}:\n\tЦвет: {}\n\tДлина стороны: {}\n\tПлощадь: {}\n'
        return tpl.format(self.name, self.color, self.width, self.area)

    # Let's overload so that when one side changes, the square remains square
    width = property(Rectangle.width_get, length_set, None, 'Length')
    height = property(Rectangle.height_get, length_set, None, 'Length')
