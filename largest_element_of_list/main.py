'''
For a given list, get the sum of each number in the list
'''
give_list = [1,-23,53,2,6,345,234]

def largest_from_list(lst):
  largest = lst[0] #setting first number to largest to check the condition
  for num in lst:
    if num > largest:
      largest = num #after checking condition if true assign new large value to varible 'largest' if not proceed to next
  return f'Largest number from given list {largest}'
    

print(largest_from_list(give_list))