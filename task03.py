with open('task3.txt', 'r') as file:
    lines = file.readlines()
    salaries = []  # подготавливаем список для зарплат
    counter = 0  # счетчик для кол-ва сотрудников ака кол-ва строк в файле (если я правильно прочитал условие, конечно)
    for line in lines:
        name, salary = line.split(' ')  # отделяем имена от окладов
        if int(salary) < 20000:
            print(f'У сотрудника {name} зарплата ниже 20000!')
        salaries.append(int(salary))  # собираем все оклады в один список
        counter += 1
    # потом суммируем получившийся список и делим его на каунтер ака кол-во сотрудников. округление для красоты
    print(f'Средний размер зарплаты в конторе {(sum(salaries) / counter).__round__(2)}')
