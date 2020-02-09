from random import randint, choice


class Car:
    def __init__(self, speed: int, color: str, name: str, is_police: bool):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        print(f'{self.name} поехала')

    def stop(self):
        print(f'{self.name} остановилась')

    def turn(self, direction: str):
        print(f'{self.name} повернула {direction}')

    def show_speed(self):
        current_speed = randint(0, self.speed)
        print(f'Текущая скорость автомобиля - {current_speed} км/ч.')


class TownCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        current_speed = randint(0, self.speed)
        if current_speed > 60:
            print(f'Ваша скорость - {current_speed}, это превышает лимит в 60 км/ч! Нарушаем!')
        else:
            print(f'Текущая скорость автомобиля - {current_speed} км/ч.')


class SportsCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)


class WorkCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        current_speed = randint(0, self.speed)
        if current_speed > 40:
            print(f'Ваша скорость - {current_speed}, это превышает лимит в 40 км/ч! Нарушаем!')
        else:
            print(f'Текущая скорость автомобиля - {current_speed} км/ч.')


class PoliceCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)


def show_info(car: Car):  # мне показалось, что реализовать отображение инфы проще отдельной функцией
    if not car.is_police:
        print(f'{car.name}, цвет - {car.color}, максимальная скорость - {car.speed}. Это полицейский автомобиль')
    else:
        print(f'{car.name}, цвет - {car.color}, максимальная скорость - {car.speed}.')
    car.go()
    car.show_speed()
    direction = choice(['направо', 'налево'])
    car.turn(direction)
    car.stop()


if __name__ == '__main__':
    car1 = TownCar(100, 'Белый', 'Лада Калина', False)
    show_info(car1)
    car2 = SportsCar(300, 'Красный', 'Тупо Феррари', False)
    show_info(car2)
    car3 = WorkCar(60, 'Оранжевый', 'Снегоуборочная машина', False)
    show_info(car3)
    car4 = PoliceCar(100, 'Бело-синий', 'Бобик', True)
    show_info(car4)
