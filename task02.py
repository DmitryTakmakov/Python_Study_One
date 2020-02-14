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
        while True:
            try:
                v = float(input('Введите размер пальто.\n'))
            except ValueError:
                print('Вы ввели недопустимое значение, попробуйте еще раз. Размер нужно вводить в цифрах, через точку.')
            else:
                fabric_volume = (v / 6.5) + 0.5
                break
        return fabric_volume.__round__(2)


class Suit(Clothes):
    def __init__(self, name='костюм'):
        self.name = name

    @property
    def fabric_volume(self):
        while True:
            try:
                h = float(input('Введите рост в метрах.\n'))
            except ValueError:
                print('Вы ввели недопустимое значение. Рост нужно вводить в цифрах, через точку. Попробуйте еще раз.')
            else:
                fabric_volume = (2 * h) + 0.3
                break
        return fabric_volume.__round__(2)


if __name__ == '__main__':
    c1 = Coat()
    c2 = Suit()
    vol1 = c1.fabric_volume
    print(f'На такое пальто потребуется {vol1} м. ткани.')
    vol2 = c2.fabric_volume
    print(f'На такой костюм потребуется {vol2} м. ткани.')
    print(f'Всего потребуется {(vol1 + vol2).__round__(2)} м. ткани.')
