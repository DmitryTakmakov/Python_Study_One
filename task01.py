file = open('task1.txt', 'a')
while True:
    user_input = input('Введите что угодно. Если хотите остановиться, то просто нажмите Enter в пустой строке.\n')
    if user_input == '':
        file.close()
        break
    else:
        file.write(user_input + '\n')
