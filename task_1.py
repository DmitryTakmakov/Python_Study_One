str_var = "Hello!"
print(f'{str_var} - I am a {type(str_var)} variable')
int_var = 2151253
print(f'{int_var} - I am a {type(int_var)} variable')
float_var = 14.115
print(f'{float_var} - I am a {type(float_var)} variable')
bool_var = True
print(f'{bool_var} - I am a {type(bool_var)} variable')
list_var = ['I', 'hold', 'various', 'things', 214, 67278.9898, False]
print(f'{list_var} - I am a {type(list_var)} variable')
tuple_var = ('I', 'hold', 'things', 'too', 'but I can not be modified!')
print(f'{tuple_var} - I am a {type(tuple_var)} variable')
dict_var = {"first": 1, "second": 2, "third": 3}
print(f'{dict_var} - I am a {type(dict_var)} variable')
user_input = input("Hi, there! Write something:\n")
print(user_input)
user_number = int(input('Okay now, how about a number?\n'))
print('Check this out, I can divide it by two', user_number / 2)
