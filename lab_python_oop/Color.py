from lab_python_oop import Exceptions as e


class Color:

    # Just for fun, let's make it as unusual as possible
    allowed = {'red': 'красный', 'green': 'зеленый', 'blue': 'синий'}
    color = property()

    def __init__(self, color):
        self.color = color

    def __repr__(self):
        # Translate only if printed
        return str(Color.allowed[self.__color])

    @color.getter
    def color(self):
        return str(self.__color)

    @color.setter
    def color(self, value):
        if value not in Color.allowed:
            raise e.BadArguments('Not allowed color value')
        self.__color = value

    @color.deleter
    def color(self):
        del self.__color
