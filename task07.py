from math import factorial


def my_fibo_gen():
    for i in range(15):
        n = factorial(i)
        yield n


for el in my_fibo_gen():
    print(el)
