from itertools import count, cycle


def endless_iter():
    number = int(input('Пожалуйста, введите целое число\n'))
    for i in count(number, 1):
        print(i)


def endless_cycle():
    user_list = []
    while True:
        user_input = input('Давайте заполним список. Введите число. Если вы закончили, введите +\n')
        if user_input == '+':
            break
        elif not user_input.isdigit():
            print('Это не число')
        else:
            user_list.append(int(user_input))
    print('А теперь страдайте, наблюдая за бесконечным повторением этого списка!')
    for i in cycle(user_list):
        print(i)


if __name__ == '__main__':
    endless_iter()
    endless_cycle()
