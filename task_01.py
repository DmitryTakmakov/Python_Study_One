def non_zero_del(var1, var2):
    """
    Деление двух чисел за исключением нуля.
    :param var1: int, float
    :param var2: int, float
    :return: float, str if zero
    """
    try:
        result = var1 / var2
    except ZeroDivisionError:
        return "Вы разделили на ноль и перешли на следующий уровень бытия! Поздравляю!"
    else:
        return result


temp = non_zero_del(int(input('Введите делимое:\n')), int(input('Введите делитель:\n')))
print(temp)