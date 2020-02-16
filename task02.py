from random import randint


class DividedByZeroError(Exception):
    def __init__(self, text='На ноль делить нельзя'):
        self.__text = text

    def __str__(self):
        return self.__text


while True:
    a = randint(1, 100)
    print(f'Наше делимое - {a}.')
    try:
        b = int(input('Введите какое-нибудь число:\n'))
        if b == 0:
            raise DividedByZeroError
    except DividedByZeroError as e:
        print(e)
    else:
        print(a / b)
        break
