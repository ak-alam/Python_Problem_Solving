"""
It's the end of the semester and you got your grades from three classes: Geometry, Algebra, and Physics.
Create a program that:

Reads the grades of these 3 classes (Grades range from 0 - 10)
Calculate the average of your grades
Example: Geometry = 6, Algebra = 7, Physics = 8
Output: average_score = 7

-> modified above question
If the average score is 7 and above print "Good job!", if the average score is between 6 and 4 print "You need to work harder!", if the average score is below 4 print "Failed, you really need to work harder!".
"""
geometry_grade = int(input('Enter Your grade range from 0 - 10: ' ))
algebra_grade = int(input('Enter Your grade range from 0 - 10: ' ))
physics_grade = int(input('Enter Your grade range from 0 - 10: ' ))

average_score  = (geometry_grade + algebra_grade + physics_grade) // 3

#from here onwards the modified code starts.

if average_score >= 7:
  print(f"You'r average score is {average_score}, Good job!")
elif average_score >= 4 and average_score <= 6:
  print(f"You'r average score is {average_score},You need to work harder!")
else:
  print(f"You'r average score is {average_score},Failed, you really need to work harder!")