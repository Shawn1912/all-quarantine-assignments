from math import pi

class Circle:
    """This class is a template of
	attributes and methods of a circle"""

    def __init__(self, radius):
        self.r = radius

    def area(self):
        a = pi * r * r
        print("Area of circle is {} sq. units".format(round(a, 3)))

    def perimeter(self):
        p = 2 * pi * r
        print("Perimeter of circle is {} units".format(round(p, 3)))

r = int(input("Enter radius (in units) of circle : "))

c = Circle(r)
c.area()
c.perimeter()
