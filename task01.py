def unpacked(list):
    """
    Эта функция нужна для выдирания значений из меньших списков, составляющих матрицу
    :param list: list
    :return: str
    """
    partial = ''
    for itm in list:
        partial += ''.join(str(itm)) + ' '
    return partial


class Matrix:
    """
    Класс для всяких муток с матрицами. Вводите сюда списки списков, пожалуйста, по-хорошему прошу!
    """

    def __init__(self, data: list):
        self.data = data

    def __str__(self):  # Сергей, признаюсь честно - я безбожно стырил (НО ДОРАБОТАЛ) эту конструкцию у вас из игры
        matrix_str = ''
        for value in self.data:
            matrix_str += ''.join(unpacked(value)) + '\n'
        return matrix_str

    def __add__(self, other):
        new_matrix = ''  # это матрица для результата сложения
        temp_line = ''  # временное хранилище для строк
        for value1, value2 in zip(self.data, other.data):  # перебираем обе матрицы
            for itm1, itm2 in zip(value1, value2):  # перебираем элементы в каждой строке исходных матриц
                temp_line += ''.join(str(itm1 + itm2)) + ' '  # вот тут мы их суммируем
            new_matrix += temp_line + '\n'  # как только заканчивается элементы строки - перенос
            temp_line = ''  # очищаем хранилище
        return new_matrix


if __name__ == '__main__':
    m1 = Matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]])  # в задании не было указано, откуда берутся эти списки списков,
    # поэтому я решил просто задать их в коде
    m2 = Matrix([[11, 12, 13], [14, 15, 16], [17, 18, 19]])
    print(m1)
    print(m2)
    print(m1 + m2)
