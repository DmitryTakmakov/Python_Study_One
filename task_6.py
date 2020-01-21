a = float(input('Please enter number A:\n'))
b = float(input('Please enter number B:\n'))
day = 1
while a < b:
    a = a + a * 0.1
    day += 1
print(day)
