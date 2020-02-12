from abc import ABC, abstractmethod


class Clothes(ABC):

    @abstractmethod
    def fabric_volume(self, size):
        pass


class Coat(Clothes):
    def __init__(self, name='coat'):
        self.name = name

    def fabric_volume(self, v):
        v = float(input('Введите размер пальто.\n'))
        fabric_volume = (v / 6.5) + 0.5
        return fabric_volume


class Suit(Clothes):
    def __init__(self, name='suit'):
        self.name = name

    def fabric_volume(self, h):
        h = float(input('Введите рост.\n'))
        fabric_volume = (2 * h) + 0.3
        return fabric_volume


c1 = Coat('palto')
v = c1.fabric_volume(4)
print(v)
