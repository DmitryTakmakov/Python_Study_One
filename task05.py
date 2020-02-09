class Stationery:
    def __init__(self, title):
        self.title = title

    def draw(self):
        print('Запуск отрисовки')


class Pen(Stationery):
    def __init__(self, title):
        super().__init__(title)

    def draw(self):
        print(f'{self.title} начинает отрисовку!')


class Pencil(Stationery):
    def __init__(self, title):
        super().__init__(title)

    def draw(self):
        print(f'{self.title} начинает отрисовку! Графика incoming!')


class Sharpie(Stationery):  # маркер, которым рисуют, по-английски называется таки sharpie
    def __init__(self, title):
        super().__init__(title)

    def draw(self):
        print(f'{self.title} начинает отрисовку! Черкаемся на полях!')


if __name__ == '__main__':
    my_pen = Pen('Ручка')
    my_pen.draw()
    my_pencil = Pencil('Карандаш')
    my_pencil.draw()
    my_sharpie = Sharpie('Маркер')
    my_sharpie.draw()
