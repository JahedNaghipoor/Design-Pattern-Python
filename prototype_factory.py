# Prototype
from copy import deepcopy


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


class PersonFactory:
    main_office_person = Person('', Address('', 'Offenbach am Main', 'Germany'))
    aux_office_person = Person('', Address('', 'Offenbach am Main', 'Germany'))

    @staticmethod
    def __new_person(proto, name, street):
        result = deepcopy(proto)
        result.name = name
        result.address.street = street
        return result

    @staticmethod
    def new_main_address(name, street):
        return PersonFactory.__new_person(PersonFactory.main_office_person, name, street)

    @staticmethod
    def new_aux_address(name, street):
        return PersonFactory.__new_person(PersonFactory.aux_office_person, name, street)


if __name__ == '__main__':

    p1 = PersonFactory.new_main_address('Jahed', 'Friedhofstrasse 54')
    p2 = PersonFactory.new_aux_address('Atefeh', 'Friedhofstrasse 56')
    print(p1)
    print(p2)


