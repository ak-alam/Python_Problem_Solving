'''
Take two numbers from the users. Calculate the result of second number power of the first number.
'''
from math import pow
first_number = int(input('Enter First Value: '))
second_number = int(input('Enter Second Value: '))

math_power = first_number ** second_number #2nd num power of 1st num

#we can also use buildin function pow from math module
result = pow(first_number, second_number) #using the buildin function power

print(f'{second_number} power of the {first_number} is, {result}')