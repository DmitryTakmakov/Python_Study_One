line_counter = 0
word_counter = 0
with open('task2.txt', 'r') as file:
    for line in file:
        word_counter = line.count(' ') + 1  # считаем количество слов как кол-во пробелов + 1
        line_counter += 1
        print(f'В строке {line_counter} - {word_counter} слов')
