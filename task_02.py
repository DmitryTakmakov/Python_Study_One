def data_printer(**kwargs) -> str:
    """ Переформатирует принимаемые на вход данные

    :param kwargs: str
    :return: str
    """
    line = ''
    for kw, args in kwargs.items():
        line += f'{kw}: {args}, '
    return line


# создаем шаблон для заполнения формы и указываем в ней ожидаемый типа данных
user_answer_template = {
    'имя': '',
    'фамилия': '',  # признаюсь честно, я так и не нашел, как можно просклонять слово в цикле без установки pymorphy,
                    # который показался мне слегка избыточным для данной задачи
    'год рождения': '',
    'город проживания': '',
    'адрес эл. почты': '',
    'номер телефона': ''
}
# теперь заполняем форму
for key in user_answer_template.keys():
    user_answer = input(f'Пожалуйста, введите {key}:\n')
    user_answer_template[key] = user_answer
# и обрабатываем ее
print(data_printer(**user_answer_template))
