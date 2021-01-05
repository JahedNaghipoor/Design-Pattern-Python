# Dependency Inversion Principle
from abc import abstractmethod
from enum import Enum


class Relationship(Enum):
    PARENT = 0
    CHILD = 1
    SIBLING = 2


class Person:
    def __init__(self, name):
        self.name = name


class RelationshipBrowser:
    @abstractmethod
    def find_all_children_of(self, name):
        pass


class Relationships(RelationshipBrowser):

    def __init__(self):
        self.relations = []

    def add_parent_and_child(self, parent, child):
        self.relations.append((parent, Relationship.PARENT, child))
        self.relations.append((child, Relationship.CHILD, parent))

    def find_all_children_of(self, name):
        for r in self.relations:
            if r[0] == name and r[1] == Relationship.PARENT:
                yield r[2].name


class Research:
    def __init__(self, browser):
        for p in browser.find_all_children_of('John'):
            print(f'John has a child called {p}')


parent1 = Person('John')
child1 = Person('Jahed')
child2 = Person('Atefeh')

relationships = Relationships()
relationships.add_parent_and_child(parent1, child1)
relationships.add_parent_and_child(parent1, child2)

Research(relationships)
