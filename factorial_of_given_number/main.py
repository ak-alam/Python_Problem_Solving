'''
Question 
Write code that will calculate 15 factorial. (factorial is product of
positive ints up to a given number. e.g 5 factorial is 5x4x3x2x1)
'''
factorial = 1
user_number = int(input("Enter number to find its factorial: "))
for i in range(1, user_number+1):
  factorial *= i

print(f'factorial of {str(user_number)} is {str(factorial)}')
