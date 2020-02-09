class Worker:
    _income = {'wage': int(), 'bonus': int()}  # в задании не очень ясно сказано, как должен быть реализован этот
    # словарь, откуда брать в него значения и т.п. ну, по логике, не может же у всех работников быть одинаковая
    # зарплата и премия...

    def __init__(self, name: str, surname: str, position: str):
        self.name = name
        self.surname = surname
        self.position = position

    def get_income(self):  # функция для заполнения словаря с доходом
        self._income['wage'] = int(input('Введите размер зарплаты сотрудника.\n'))
        self._income['bonus'] = int(input('Введите размер премии сотрудника.\n'))


class Position(Worker):

    def __init__(self, name, surname, position):
        super().__init__(name, surname, position)

    def get_full_name(self):
        print(f'Работника на позиции {self.position} зовут {self.name} {self.surname}')

    def get_total_income(self):
        print(f"Полный доход этого сотрудника - {super()._income['wage'] + super()._income['bonus']}")


if __name__ == '__main__':
    vasya = Position('Евгений', 'Понасенков', 'Просто бог')
    while True:
        try:  # заполняем словарь дохода сотрудника, проверяем, чтобы нам не навводили всякой чуши
            vasya.get_income()
        except ValueError as e:
            print(f'{e}. Вы неверно указали зарплату или премию, введите их еще раз.')
            continue
        else:
            vasya.get_full_name()
            vasya.get_total_income()
            break
