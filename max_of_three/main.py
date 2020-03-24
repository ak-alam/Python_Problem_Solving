'''
Find the largest of the three numbers.
'''
first_num = int(input('Enter value :'))
sec_num = int(input('Enter value :'))
third_num = int(input('Enter value :'))

if first_num > sec_num and first_num > third_num:
  print(f'Large Number is {first_num}')
elif sec_num > first_num and sec_num > third_num:
    print(f'Large Number is {sec_num}')
elif third_num > sec_num and third_num > first_num:
    print(f'Large Number is {third_num}')
