user_time = int(input('Please enter the time in seconds:\n'))
print(f'Okay, so the time is {user_time % (3600 * 24) // 3600}:{(user_time % 3600) // 60}:{(user_time % 3600) % 60}')
