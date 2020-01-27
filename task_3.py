# решение через словарь
seasons = {'Spring': [3, 4, 5], 'Summer': [6, 7, 8], 'Autumn': [9, 10, 11], 'Winter': [12, 1, 2]}
month = int(input('Please enter a month as a number from 1 to 12:\n'))
for key, value in seasons.items():
    if month in value:
        print(key)

# решение через список
seasons_list = [['Spring', 3, 4, 5], ['Summer', 6, 7, 8], ['Autumn', 9, 10, 11], ['Winter', 12, 1, 2]]
month_list = int(input('Please enter a month as a number from 1 to 12:\n'))
for i in range(len(seasons_list)):
    if month_list in seasons_list[i]:
        print(seasons_list[i][0])
