'''
Question 1
Can you remember how to check if a key exists in a dictionary?
Using the capitals dictionary below write some code to ask the user to input
a country, then check to see if that country is in the dictionary and if it is
print the capital. If not tell the user it's not there.
'''
capitals = {'France':'Paris','Spain':'Madrid','United Kingdom':'London','India':'New Delhi','United States':'Washington DC','Italy':'Rome','Denmark':'Copenhagen','Germany':'Berlin','Greece':'Athens','Bulgaria':'Sofia','Ireland':'Dublin','Mexico':'Mexico City'}

# for key, value in capitals.items():
#   print(f'key: {key}  value: {value}')

user_country_check = input('Enter a country name:').title()

for key, value in capitals.items():
  if user_country_check == key:
    print(value)
    break
  else:
    print("It's not exits")
    break