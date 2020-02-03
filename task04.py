old_list = [1, 51, 6, 899, 817, 1, 66, 6, 899, 10, 66, 14]
new_list = [el for el in old_list if old_list.count(el) == 1]
print(new_list)
