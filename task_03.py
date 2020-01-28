def my_func(first_number: int, second_number: int, third_number: int) -> int:
    """
    Сумма двух наибольших чисел из трех
    :param first_number: int
    :param second_number: int
    :param third_number: int
    :return: int
    """
    # я предполагаю, что есть решения и получше, но пусть будет реализация через условия
    if first_number >= second_number:
        if second_number >= third_number:
            return first_number + second_number
        else:
            return first_number + third_number
    else:
        if first_number >= third_number:
            return first_number + second_number
        else:
            return second_number + third_number


# теперь запрашиваем аргументы у пользователя
numbers = []
while True:
    try:
        user_number = int(input('Введите, пожалуйста, целое число:\n'))
    except ValueError as e:
        print(f'{e}. Это не число, введите число')
    else:
        numbers.append(user_number)
        if len(numbers) > 2:  # как только в списке оказывается 3 числа цикл прекращает работу
            break
# разделяем введенные числа по переменным
a, b, c = numbers
# обрабатываем функцией
print(my_func(a, b, c))
