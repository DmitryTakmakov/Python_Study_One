user_list = []
while True:
    a = input('Please enter anything you like!\nIf you are finished type "Enough"\n')
    if a == 'Enough':
        break
    else:
        user_list.append(a)
print(f"Here's what you entered: {user_list}")

new_list1 = user_list[::2]
new_list2 = user_list[1::2]
mod_list = []
a = 0
b = 0
for i in range(int(len(user_list))):
    if i % 2 == 0 and i <= len(new_list2):
        mod_list.append(new_list2[a])
        a += 1
    else:
        mod_list.append(new_list1[b])
        b += 1
print(mod_list)
