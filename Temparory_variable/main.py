'''
Swap two variables.

To swap two variables: the value of the first variable will become the value of the second variable. On the other hand, the value of the second variable will become the value of the first variable. '''

var_swap1 = int(input('Enter a Value: '))
var_swap2 = int(input('Enter a Value: '))

print(f'Values before swap first vaule: {var_swap1}, second value: {var_swap2}')

# var_swap1, var_swap2 = var_swap2, var_swap1 #here we using tuple to swap values

# print(f'Values after swap first value: {var_swap1}, second value: {var_swap2}')

''' 
Here's another method we can swap values using simple maths
'''



var_swap1 = var_swap1 + var_swap2 #adding both values and storing value back to first variable 
var_swap2 = var_swap1 - var_swap2 #subtracting values and storing values back to second varible
var_swap1 = var_swap1 - var_swap2 #substracting values and storing values back to first variable

print(f'Values after swap first value: {var_swap1}, second value: {var_swap2}')
