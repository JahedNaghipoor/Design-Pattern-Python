# Monostate (Not recommended, instead use metaclass or decorator)

class CEO:
    __shared_state = {
        "name": "Steve",
        "age": 55
    }

    def __init__(self):
        self.__dict__ = self.__shared_state

    def __str__(self):
        return f" {self.name} is {self.age} years old"


class Monostate:
    _shared_state = {}

    def __new__(cls, *args, **kwargs):
        obj = super(Monostate, cls).__new__(cls, *args, **kwargs)
        obj.__dict__ = cls._shared_state
        return obj


class CFO(Monostate):
    def __init__(self):
        self.name = ''
        self.money = 0

    def __str__(self):
        return f"{self.name} manages {self.money}"


if __name__ == '__main__':
    cfo1 = CFO()
    cfo1.name = "Jahed"
    cfo1.money = 10
    print(cfo1)

    cfo2 = CFO()
    cfo2.name = "Atefeh"
    cfo2.money = 11
    print(cfo2)
    print(cfo1, cfo2, sep='-')
