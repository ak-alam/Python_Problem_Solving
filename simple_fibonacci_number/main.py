'''
Question 7
Write code to calculate Fibonacci numbers. Create list containing
first 20 Fibonacci numbers, (Fib  numbers made by sum of preceeding
two. Series starts 0 1 1 2 3 5 8 13 ....)
'''
user_number = int(input('Enter number: '))
#initial values in the sequence
first_value = 0
second_value = 1

fib_list = []
for i in range(user_number):
  fib_list.append(first_value)
  first_value, second_value = second_value ,first_value + second_value

print(fib_list)

