'''
Take two inputs from the user. One will be an integer. The other will be a float number. Then multiply them to display the output.
'''


def input_to_number(): 
  '''
  returning product of values
  '''
  first_input = input('Enter value: ')
  second_input = input('Enter value: ')

  result = int(first_input) * float(second_input)

  return result


print(input_to_number())