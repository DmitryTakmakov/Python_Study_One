eng_ru = {
    'One': 'Один',
    'Two': 'Два',
    'Three': 'Три',
    'Four': 'Четыре'
}
# небольшой словарик для облегчения задачи
with open('task4.txt', 'r') as file:
    lines = file.readlines()  # разбиваем исходный файл на отдельные строки
    for line in lines:
        word, number = line.split(' - ')  # разбиваем каждую отдельную строку на составляющие
        for key, value in eng_ru.items():  # проходимся циклом по словарю и ищем соответствия
            if key == word:  # если слово совпадает с английским числительным (ключом словаря) меняем его на русское
                word = value
                with open('task4_new.txt', 'a') as new_file:  # собираем новый файл
                    new_file.write(word + ' - ' + number)
