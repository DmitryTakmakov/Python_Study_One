class Cell:
    def __init__(self, cells: int):
        self.__cells = cells

    def __add__(self, other):
        if isinstance(self, Cell) and isinstance(other, Cell):  # проверяем, чтобы оба объекта были клетками
            return self.__cells + other.__cells
        else:
            print('Это не клетки, и сложить их я не могу!')

    def __sub__(self, other):
        if isinstance(self, Cell) and isinstance(other, Cell):
            if self.__cells - other.__cells <= 0:
                print('Так сделать нельзя, в первой клетке ячеек меньше, чем во второй')
            else:
                return self.__cells - other.__cells
        else:
            print('Это не клетки, и вычесть их друг из друга я не могу!')

    def __mul__(self, other):
        if isinstance(self, Cell) and isinstance(other, Cell):
            return self.__cells * other.__cells
        else:
            print('Это не клетки, и умножить их я не могу!')

    def __truediv__(self, other):
        if isinstance(self, Cell) and isinstance(other, Cell):  # к сожалению, я не понял, как избежать копирования
            # кода в данных методах
            return self.__cells // other.__cells
        else:
            print('Это не клетки, и поделить их друг на друга я не могу!')

    def make_order(self, row_length: int):  # по сути, я реализовал этот метод как печать матриц из первого задания
        cell_str = ''
        for i in range(self.__cells // row_length):
            cell_str += ''.join('*' * row_length) + '\n'
        if self.__cells % row_length == 0:  # с одним отличием - добавилась проверка на целочисленное деление
            return cell_str
        else:
            cell_str += ''.join('*' * (self.__cells % row_length))  # чтобы вот тут не джойнилось 0 ячеек
            return cell_str


if __name__ == '__main__':
    c1 = Cell(15)
    c2 = Cell(19)
    print(c1 + c2)
    print(c1 - c2)
    print(c1 * c2)
    print(c1 / c2)
    print(c1.make_order(3))
    print(c2.make_order(5))
