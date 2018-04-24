import math


# This is examplary class
class Point:
    # This is constructor
    # Every method from class, needs to have self, as a first argument
    # (it tells Python that this method belongs to the class)
    def __init__(self, x, y):
        self.x = x  # attributes
        self.y = y

    # typical method
    def distance_from_origin(self):
        return math.hypot(self.x, self.y)

    # override of ==
    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    # override of str(X)
    def __str__(self):
        return "Pxy = ({0.x}, {0.y})".format(self)

    # override of +
    def __add__(self, other):
        return self.x + other.x, self.y + other.y


# Now Point is a base class, so Circle inherits from Point
class Circle(Point):
    def __init__(self, radius, x=0, y=0):
        super().__init__(x, y)
        self.radius = radius

    def area(self):
        return math.pi * (self.radius ** 2)


if __name__ == '__main__':
    P1 = Point(3, 4)
    P2 = Point(8, 10)

    print("Distance from (0,0): %f" % P1.distance_from_origin())
    print("Is P1 equal to P2? %s" % (P1 == P2))
    print(str(P1))
    print("P1 + P2 (as vectors) = " + str((P1 + P2)))

    C1 = Circle(2)
    print("Area of circle with r=2 is %f" % C1.area())
