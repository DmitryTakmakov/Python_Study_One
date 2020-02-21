def validator(data, type):
    if isinstance(data, type):
        return data
    else:
        print(f'Вы ввели неверный тип данных: {data} должен быть {type}')


class Warehouse:
    __total_volume = 1000000  # это полный объем склада, он же не бесконечный. и да, это просто рандомное число

    def __init__(self, name):
        self.name = name
        self.__warehouse = []  # по аналогии с гаражом из седьмого урока - список как хранилище данных

    @property
    def add_to_warehouse(self):
        return tuple(self.__warehouse)

    @add_to_warehouse.setter
    def add_to_warehouse(self, other):
        try:
            if self.__total_volume - other.size * other.quantity <= 0:
                raise ArithmeticError
        except ArithmeticError:
            print(f'{other.brand}, {other.quantity} - на складе нет места под такое количество товара!')
        except TypeError:
            print('Либо размер, либо количество товара были указаны неверно, пожалуйста, проверьте.')
        else:
            self.__warehouse.append(other.dict_store)
            self.__total_volume -= other.size * other.quantity

    def __str__(self):
        return str(self.__warehouse)


class OfficeAutomation:
    def __init__(self, brand: str, size: int, quantity: int):  # под size подразумевается объемный вес, габариты
        # товара. ИРЛ была бы отдельная функция для рассчета этого, но для упрощения будем просто заносить его как
        # число
        self.brand = validator(brand, str)  # кстати, указание типа при инициализации класса, в принципе, работает
        # как валидатор, однако, да, должен признать, что в реальных условиях пользователь не будет задавать значения
        # прямо в коде
        self.size = validator(size, int)
        self.quantity = validator(quantity, int)


class Printer(OfficeAutomation):
    def __init__(self, color: bool, brand, size, quantity):  # цветной принтер или нет - булево выражение
        self.color = validator(color, bool)
        super().__init__(brand, size, quantity)
        self.dict_store = {'brand': self.brand,
                           'size': self.size,
                           'quantity': self.quantity,
                           'color': self.color}


class Scanner(OfficeAutomation):
    def __init__(self, brand, size, quantity):  # может быть, дело в моей бедной фантазии, но я хоть убей не могу
        # представить, какие еще параметры у сканнера могут заинтересовать СКЛАД, а не конечных пользователей
        super().__init__(brand, size, quantity)
        self.dict_store = {'brand': self.brand,
                           'size': self.size,
                           'quantity': self.quantity}


class Copier(OfficeAutomation):
    def __init__(self, brand, size, quantity):
        super().__init__(brand, size, quantity)
        self.dict_store = {'brand': self.brand,
                           'size': self.size,
                           'quantity': self.quantity}


warehouse = Warehouse('sklad')
scanner = Scanner('Panasonic', 11, 2000000)
printer = Printer(True, 'Canon', 80, 100)
copier = Copier(125215135, 200, 11)
warehouse.add_to_warehouse = scanner
warehouse.add_to_warehouse = printer
warehouse.add_to_warehouse = copier
print(warehouse)
