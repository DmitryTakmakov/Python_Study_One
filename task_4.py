user_number = input('Please enter a whole, positive number:\n')
i = 0
n = 0
while i < len(user_number):
    if int(user_number[i]) >= n:
        n = int(user_number[i])
    i += 1
print(n)
