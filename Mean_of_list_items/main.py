'''
Ask the user to input a sequence of numbers. Then calculate the mean
and print the result
'''
def mean_of_list():
  seq_numbr = []
  list_sum = 0
  while True:
    user_number = input('Enter number and "q" to quit: ')
    if user_number == 'q':
      break
    user_number = int(user_number)  
    seq_numbr.append(user_number)

  for num in seq_numbr:
    list_sum += num
  mean = list_sum / len(seq_numbr)
  print("sequence of list: ",seq_numbr)  
  print("Sum of list items:", list_sum)
  print("Mean of list items: ", mean)

mean_of_list()