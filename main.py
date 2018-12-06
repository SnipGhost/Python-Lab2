import lab_python_oop.Exceptions as e
from lab_python_oop.Rectangle import Rectangle
from lab_python_oop.Circle import Circle
from lab_python_oop.Square import Square

# Wow. It's raises exception :)
try:
    r = Rectangle(1, 1, 'unreal_color')
    print(r)
except e.LabException as err:
    print('Expected exception:', err)
    print()


r = Rectangle(3, 2, 'blue')
print(r)

c = Circle(5, 'green')
print(c)

s = Square(5, 'red')
print(s)


# How do you like that, Elon Musk?
s.width = 10
# Spoiler: everything is ok.
# Because I overloaded the properties
print(s)
