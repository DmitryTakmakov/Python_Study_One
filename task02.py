from abc import ABC, abstractmethod


class Clothes(ABC):

    @abstractmethod
    def fabric_volume(self):
        pass


class Coat(Clothes):
    def __init__(self, name='пальто'):
        self.name = name

    @property
    def fabric_volume(self):
        v = float(input('Введите размер пальто.\n'))
        fabric_volume = (v / 6.5) + 0.5
        return f'Чтобы сшить {self.name} такого размера потребуется {fabric_volume.__round__(2)} м. ткани.'


class Suit(Clothes):
    def __init__(self, name='костюм'):
        self.name = name

    @property
    def fabric_volume(self):
        h = float(input('Введите рост в метрах.\n'))
        fabric_volume = (2 * h) + 0.3
        return f'Чтобы сшить {self.name} на такой рост потребуется {fabric_volume.__round__(2)} м. ткани.'


if __name__ == '__main__':
    c1 = Coat()
    c2 = Suit()
    vol1 = c1.fabric_volume
    print(vol1)
    vol2 = c2.fabric_volume
    print(vol2)
