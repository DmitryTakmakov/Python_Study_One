from sys import argv


script_name, work_load, per_hour, benefit = argv
print("Название программы: ", script_name)
print('Выработка в часах: ', work_load)
print('Ставка в час: ', per_hour)
print('Премия: ', benefit)
print('Всего заработная плата: ', int(work_load) * int(per_hour) + int(benefit))
