# первый метод. признаться, я так и не понял, как им решить без использования цикла
def my_func(x: float, y: int) -> float:
    """
    Возведение числа в степень без использования встроенной функции
    :param x: float
    :param y: int
    :return: float
    """
    result = 1
    for i in range(abs(y)):
        result *= 1 / x
    return result


# второй метод я так и не понял, как реализовать, к сожалению.


# запрашиваем у пользователя первое число, оно должно быть положительным
while True:
    try:
        a = float(input('Введите действительное положительное число:\n'))
        if a <= 0:
            raise ZeroDivisionError
    except ZeroDivisionError as e:
        print(f'{e}. Число должно быть больше нуля.')
    except ValueError as v:
        print(f'{v}. Вы ввели что-то непонятное.')
    else:
        break
# запрашиваем у пользователя второе число, оно должно быть целым и отрицательным
while True:
    try:
        b = int(input('Введите целое отрицательное число:\n'))
        if b >= 0:
            raise IndexError
    except IndexError as ie:
        print(f'{ie}. Число должно быть меньше нуля')
    except ValueError as v:
        print(f'{v}. Вы ввели что-то непонятное.')
    else:
        break
# теперь обрабатываем числа
print(my_func(a, b))
