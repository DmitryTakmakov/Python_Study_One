class Road:
    def __init__(self, _length: float, _width: float):  # флоуты потому что может потребоваться разные длина и
        # ширина, не только целочисленные.
        self._length = _length
        self._width = _width

    def asphalt(self):
        asphalt_volume = (self._length * self._width * 25 * 5) / 1000  # судя по информации из гугла, 25 кг и 5 см -
        # это стандартные величины, которые определены ГОСТом. поэтому отдельно их запрашивать нет смысла.
        print(f'Для укладки такой дороги потребуется {asphalt_volume.__round__(2)} тонн асфальта')


if __name__ == '__main__':
    length = float(input('Введите необходимую длину дороги в метрах:\n'))
    width = float(input('Введите необходимую ширину дороги в метрах:\n'))
    sample_road = Road(length, width)
    sample_road.asphalt()
