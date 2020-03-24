'''
For a given list, get the sum of each number in the list
'''
given_lst = [11,12,657,235,845]

def sum_of_list(lst):
  sum = 0
  for num in given_lst: #iterting through list
    sum += num  #adding values one by one from list

  return f'Sum of values from list : {sum}'

print(sum_of_list(given_lst))