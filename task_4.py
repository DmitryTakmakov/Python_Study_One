user_str = input('Say something funny! Two words min.\n')
user_str = user_str.split(' ')
for idx, itm in enumerate(user_str, 1):
    print(f'{idx}. {itm[:10]}')
