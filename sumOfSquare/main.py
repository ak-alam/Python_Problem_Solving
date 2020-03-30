'''
Take a number as input. Then get the sum of the numbers. If the number is n. Then get

0^2+1^2+2^2+3^2+4^2+.............+n^2
'''
user_number = int(input('Enter Number: '))

sum = 0
for number in range(user_number + 1):
  square = number ** 2
  sum = sum + square
  
print(f'Sum of the square {user_number} is {sum}')
