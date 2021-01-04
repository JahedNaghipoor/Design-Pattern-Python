# Open-Closed Principle, Open for extension, but closed for modification
from enum import Enum


class Color(Enum):
    RED = 1
    GREEN = 2
    BLUE = 3


class Size(Enum):
    SMALL = 1
    MEDIUM = 2
    LARGE = 3


class Product:
    def __init__(self, name, color, size):
        self.color = color
        self.name = name
        self.size = size


# Specification
class Specification:
    def is_satisfied(self, item):
        pass

    def __and__(self, other):
        return AndSpecification(self, other)

    def __or__(self, other):
        return OrSpecification(self, other)


class Filter:
    def filter(self, items, spec) -> object:
        pass


class ColorSpecification(Specification):
    def __init__(self, color):
        self.color = color

    def is_satisfied(self, item):
        return item.color == self.color


class SizeSpecification(Specification):
    def __init__(self, size):
        self.size = size

    def is_satisfied(self, item):
        return item.size == self.size


class AndSpecification(Specification):
    def __init__(self, *args):
        self.args = args

    def is_satisfied(self, item):
        return all(map(lambda spec: spec.is_satisfied(item), self.args))


class OrSpecification(Specification):
    def __init__(self, *args):
        self.args = args

    def is_satisfied(self, item):
        return any(map(lambda spec: spec.is_satisfied(item), self.args))


class BetterFilter(Filter):
    def filter(self, items, spec):
        for item in items:
            if spec.is_satisfied(item):
                yield item


if __name__ == '__main__':
    apple = Product('Apple', Color.GREEN, Size.SMALL)
    tree = Product('Tree', Color.GREEN, Size.LARGE)
    house = Product('House', Color.BLUE, Size.LARGE)

    products = [apple, tree, house]

    bf = BetterFilter()

    green = ColorSpecification(Color.GREEN)
    blue = ColorSpecification(Color.BLUE)
    red = ColorSpecification(Color.RED)

    small = SizeSpecification(Size.SMALL)
    medium = SizeSpecification(Size.MEDIUM)
    large = SizeSpecification(Size.LARGE)

    print('green items')
    for p in bf.filter(products, green):
        print(f' - {p.name} is green')

    print('large items')
    for p in bf.filter(products, large):
        print(f' - {p.name} is large')

    print('First method: large and blue items')
    large_blue = AndSpecification(large, blue)
    for p in bf.filter(products, large_blue):
        print(f' - {p.name} is large and blue')

    print('Second method: large and blue items')
    for p in bf.filter(products, large & blue):
        print(f' - {p.name} is large and blue')

    print('Second method: large or blue items')
    for p in bf.filter(products, small | green):
        print(f' - {p.name} is small or green')
