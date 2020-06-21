class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    @property
    def width(self):
        print("getting width")
        return self._width

    @width.setter
    def width(self, width):
        if type(width) == int or type(width) == float:
            if width <= 0:
                raise ValueError("Width must be positive!")
            else:
                self._width = width
        else:
            raise ValueError("Width be a 'int' or 'float'!")

    @property
    def height(self):
        print("getting height")
        return self._height

    @height.setter
    def height(self, height):
        if type(height) == int or type(height) == float:
            if height <= 0:
                raise ValueError("Height must be positive!")
            else:
                self._height = height
        else:
            raise ValueError("Height must be 'int' or 'float'!")

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return (self.width * 2) + (self.height * 2)

    def __str__(self):
        return "Rectangle: width = {0}, height = {1}".format(self._width, self._height)

    def __repr__(self):
        return "Rectangle({0}, {1})".format(self._width, self._height)

    def __eq__(self, other):
        if isinstance(other, Rectangle):
            return self.width == other.width and self.height == other.height
        else:
            return NotImplemented

    def __lt__(self, other):
        if isinstance(other, Rectangle):
            return self.area() < other.area()
        else:
            return NotImplemented

    def __gt__(self, other):
        if isinstance(other, Rectangle):
            return self.area() > other.area()
        else:
            return NotImplemented
