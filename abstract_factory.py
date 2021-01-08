from abc import ABC
from enum import Enum, auto


class HotDrink(ABC):
    def consume(self):
        pass


class Tea(HotDrink):
    def consume(self):
        print('this is a nice tea')


class Coffee(HotDrink):
    def consume(self):
        print('this is a nice coffee')


class HotDrinkFactory(ABC):
    def prepare(self, amount):
        pass


class TeaFactory(HotDrinkFactory):

    def prepare(self, amount):
        super().prepare(amount)
        print(f'Tea: pour {amount}ml')
        return Tea()


class CoffeeFactory(HotDrinkFactory):

    def prepare(self, amount):
        super().prepare(amount)
        print(f'Coffee: pour {amount}ml')
        return Coffee()


def make_drink(type):
    if type == 'tea':
        return TeaFactory().prepare(100)
    elif type == 'coffee':
        return CoffeeFactory().prepare(50)
    else:
        return None


class HotDrinkMachine:
    class AvailableDrink(Enum):
        COFFEE = auto()
        TEA = auto()

    factories = []
    initialized = False

    def __init__(self):
        if not self.initialized:
            self.initialized = True
            for d in self.AvailableDrink:
                name = d.name[0] + d.name[1:].lower()
                factory_name = name + 'Factory'
                factory_instance = eval(factory_name)()
                self.factories.append((name, factory_instance))

    def make_drink(self):
        print('Available drinks:')
        for f in self.factories:
            print(f[0])
        idx = int(input(f'Please pick a drink (0 - {len(self.factories) - 1}): '))
        amount = int(input('Specify amount: '))
        return self.factories[idx][1].prepare(amount)


if __name__ == '__main__':
    # entry = input('tea or coffee? ')
    # drink = make_drink(entry)
    # drink.consume()

    hdm = HotDrinkMachine()
    hdm.make_drink()
