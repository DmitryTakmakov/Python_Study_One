class NotANumberError(Exception):
    def __init__(self, text='Вы ввели не число, нужно ввести число.'):
        self.text = text

    def __str__(self):
        return self.text


def number_checker(user_input: str):  # скрипт для проверки того, что ввел пользователь
    if user_input.isdigit():
        return int(user_input)  # если пользователь ввел число, то оно преобразуется в соответствующий тип
    else:
        raise NotANumberError


user_list = []
while True:
    query = input('Введите следующий элемент списка, если вы ничего больше не хотите добавлять, введите stop:\n')
    if query == 'stop':
        print(user_list)
        break
    else:
        try:
            number_checker(query)
        except NotANumberError as e:
            print(e)
        else:
            user_list.append(query)
