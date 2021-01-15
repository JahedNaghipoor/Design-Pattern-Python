# Prototype
from copy import copy, deepcopy


class Person:
    def __init__(self, name, address):
        self.address = address
        self.name = name

    def __str__(self):
        return f'{self.name} lives in {self.address}'


class Address:
    def __init__(self, street, city, country):
        self.street = street
        self.city = city
        self.country = country

    def __str__(self):
        return f'{self.street}, {self.city}, {self.country}'


if __name__ == '__main__':
    p1 = Person('Jahed', Address('Friedhofstrasse, 54', 'Offenbach', 'Germany'))
    p2 = deepcopy(p1)
    p2.name = 'Atefeh'
    p2.address.street = 'Friedhofstrasse 56'
    print(p1)
    print(p2)