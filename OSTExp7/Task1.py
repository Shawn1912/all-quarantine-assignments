class Rectangle:
    """ This a Rectangle class
	which stores attributes and methods
    """

    def __init__(self, length, breadth):
        self.l = length
        self.b = breadth

    def area(self):
        a = l * b
        print("Area of rectangle is ", a)

l = int(input("Enter length of rectangle : "))
b = int(input("Enter breadth of rectangle : "))

#print(Rectangle.__doc__)

rect = Rectangle(l, b)
rect.area()
