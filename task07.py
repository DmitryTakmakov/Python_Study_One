import json

companies = []
with open('task7.txt', 'r') as file:
    lines = file.readlines()
    names = []  # список с названиями компаний, будущие ключи словаря
    margins = []  # список с прибылью компаний, будущие значения словаря
    profitable_companies = 0  # переменная для подсчета средней прибыли без учета убыточных компаний
    counter = 0  # кол-во прибыльных компаний
    for line in lines:
        name, form, profit, spend = line.split(' ')  # разбиваем на отдельные объекты
        names.append(name)
        margins.append(int(profit) - int(spend))
        if int(profit) - int(spend) >= 0:
            profitable_companies += profitable_companies
            counter += 1
    comp_dict = dict(zip(names, margins))  # собираем словарь компаний
    a_p_dict = dict(average_profit=str(profitable_companies // counter))  # второй словарь - средняя прибыль
    companies.append(comp_dict)
    companies.append(a_p_dict)  # финальный список готов, можно выгружать его в файл
with open('task7.json', 'w') as file:
    json.dump(companies, file)
