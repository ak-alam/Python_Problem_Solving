'''
Create a random number between any two number enter by user.
'''
from random import randint

first_val = int(input('Enter First Value: '))
second_val = int(input('Enter Second Value: '))

random_value = randint(first_val, second_val) #using builtin function 'randint' which take two values as arguments 
print(f'Random value between {first_val} to {second_val} : {random_value}')