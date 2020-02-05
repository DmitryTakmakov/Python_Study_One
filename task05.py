from random import randint


with open('task5.txt', 'w') as file:
    for i in range(10):  # в тексте задания нет особых пожеланий по кол-ву чисел в файле, так что пусть будет 10
        number = randint(1, 100)  # аналогично - особых пожеланий по числам нет...
        file.write(str(number) + ' ')

with open('task5.txt', 'r') as file:
    content = file.read()  # читаем файл
    content_list = content.split(' ')  # преобразуем в список
    result_list = []
    for itm in content_list:  # проходимся по этому списку и выбираем только числа
        if itm.isdigit():
            result_list.append(int(itm))
    print(sum(result_list))  # суммируем и печатаем получившийся список
