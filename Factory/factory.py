# Factory
from math import *
class Point:
    def __init__(self, x, y):
        self.y = y
        self.x = x

    def __str__(self):
        return f"x : {self.x}, y: {self.y}"


class PointFactory:
    @staticmethod
    def cartesian_point(x, y):
        return Point(x, y)

    @staticmethod
    def polar_point(rho, theta):
        return Point(rho * cos(theta), rho * sin(theta))


if __name__ == '__main__':
    p1 = PointFactory.cartesian_point(1, 2)
    p2 = PointFactory.polar_point(1, 120)

    print(p1, p2)
