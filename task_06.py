def int_func(word: str) -> str:
    """
    Функция, которая долго и мучительно преобразует слово из строчных букв в слово с заглавной буквы
    :param word: str
    :return: str
    """
    # признаюсь честно - задание с рейтингом в прошлом уроке пробило меня на такую паранойю, что вместо очевидного,
    # казалось бы, метода .title() пусть будет цикл!
    new_word = ''
    list(word)
    for i in range(len(word)):
        if i == 0:
            new_word += word[0].upper()  # можно даже индекс просто указать, поскольку нас интересует именно эта буква
        else:
            new_word += word[i]
    return new_word


def ext_func(line: str) -> str:
    """
    Функция, которая преобразует предложение из маленьких латинских букв в предложение, где каждое слово начинается с
    заглавной буквы.
    :param line: str
    :return: str
    """
    new_line = ''
    # по аналогии - преобразуем в список и работаем с ним посредством цикла for
    line_list = line.split(' ')
    for i in range(len(line_list)):
        new_line += int_func(line_list[i]) + ' '
    return new_line


# пользователь может выбрать, какую функцию задействовать
while True:
    choice = input('Слово или предложение?\n')
    if choice.lower() == 'слово':
        while True:
            try:
                user_word = input('Введите, пожалуйста, слово из маленьких латинских букв.\n')
                # проверяем, что нам ввел пользователь. я назначал более-менее подходящие по названиям ошибки,
                # хотя я понимаю, что они, на самом деле, означают другие вещи
                if user_word.isdigit():
                    raise ValueError
                elif user_word.isupper():
                    raise IndexError
                elif not user_word.isalpha():
                    raise AttributeError
                elif user_word.istitle():
                    raise NameError
            except ValueError:
                print('Не надо цифр, пожалуйста, только маленькие латинские буквы!')
            except IndexError:
                print('Зачем вы вводите слово из заглавных букв, если вас просят ввести слово из маленьких букв?')
            except AttributeError:
                print('Ну, тут вообще всего понамешано... Вам хорошо?')
            except NameError:
                print('Ну зачем, вот зачем печатать в прогу, которая преобразует первую букву в заглавную, '
                      'слово с заглавной буквы?')
            else:
                # если ввод прошел успешно, тогда и обрабатываем слово. я так понимаю, декораторы для этого и нужны?
                print(int_func(user_word))
                break
        break
    elif choice.lower() == 'предложение':
        while True:
            try:
                user_line = input('Пожалуйста, введите предложение из слов, написанных латинскими буквами в нижнем '
                                  'регистре.\n')
                # по аналогии со словом - проверяем, что пользователь ввел
                if user_line.istitle():
                    raise NameError
                elif user_line.isdigit():
                    raise ValueError
                elif user_line.isupper():
                    raise IndexError
                # с предложением я не смог выловить все ошибки, например, можно спокойно писать сюда буквы с цифрами,
                # и программа сработает. нашел только метод .isalnum(), но он не подходит, т.к. дает True как в
                # случае, если есть и буквы с цифрами, так и в случае если есть и буквы, и цифры
            except NameError:
                print(
                    'Нет, ну, серьезно, зачем вводить строку с заглавными буквами в прогу, которая преобразует ее в '
                    'строку с заглавной буквы?')
            except ValueError:
                print('Не надо цифр, пожалуйста, только маленькие латинские буквы!')
            except IndexError:
                print('НОГУ С КАПСА УБЕРИ!')
            else:
                # аналогично - если все верно, обрабатываем предложение
                print(ext_func(user_line))
                break
        break
    else:  # если введено что угодно, кроме этих двух вариантов
        print('Чё?')
