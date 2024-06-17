class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f'Point({self.x}, {self.y})'


class Point3D(Point):
    def __init__(self, x, y, z):
        super().__init__(x, y)
        self.z = z

    def __str__(self):
        return f'Point3D({self.x}, {self.y}, {self.z})'


class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def __str__(self):
        return f'Rectangle({self.width}, {self.height})'

    def __center(self):
        return self.width / 2, self.height / 2

    def grow(self, delta_width, delta_height):
        self.width += delta_width
        self.height += delta_height

    def area(self):
        return self.width * self.height


p = Point(1, 2)
print(p)

p3d = Point3D(1, 2, 3)
print(p3d)
