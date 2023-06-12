#Evan Perez
#24212505
#Python Programming
#Assignment 1

#1
name = "John Smith"
age = 25
is_student = True

#2
print('Name: ' + name)
print('Age: ' + str(age))
print('is_student: ' + str(is_student))

#3, 4
curr_year = 2023
birth_year = curr_year - age
print('Birth Year: ' + str(birth_year))

#5, 6
bio = name + ' is ' + str(age) + ' years old and is a student '
print(bio)

#7, 8, 9 , 10
shopping_list = ['Fruit', 'Juice', 'Cheese']
print(shopping_list)
shopping_list.append('Chocolate')
print(shopping_list)

#11, 12, 13, 14, 15
student_info = { 'Name' :'John Smith', 'Age' : 25, 'is_student' : True }
print(student_info)
print(student_info['Name'])
student_info['is_student'] = False
print(student_info)


