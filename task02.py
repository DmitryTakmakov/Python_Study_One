from random import randint

old_list = [randint(1, 100) for i in range(10)]
print(f"Here's a list of ten random numbers: {old_list}")
new_list = [el for el in old_list if old_list[el] > old_list[el - 1]]
print(new_list)
# я так и не понял, как это сделать с помощью генератора списка(( само условие-то выглядит понятно, но как именно в
# генераторе его сделать...
