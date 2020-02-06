from re import findall  # через regular expression меня надоумили это делать в чате

with open('task6.txt', 'r') as file:
    lines = file.readlines()
    subjects = {}  # заготавливаем пустой словарь
    for line in lines:
        subject, *hour = findall(r'^[\w ]*|\d+', line)  # ищем нужные паттерны в строке
        hours = sum(map(int, hour))  # суммируем все часы
        discipline = {subject: hours}  # отдельный промежуточный словарь по каждой дисциплине
        subjects.update(discipline)
print(subjects)
