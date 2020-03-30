'''
For a list, find the second largest number in the list.
'''

lst = [1,3,9,3,7,4,5]
largest = lst[0]
sec_largest = lst[0]
for i in lst:
  if i > largest:
    largest = sec_largest
    largest = i 
  elif i > sec_largest:
    sec_largest = i

print(f'Largest Number: {sec_largest}')

