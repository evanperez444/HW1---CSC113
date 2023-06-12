#Evan Perez
#24212505
#Python Programming
#Assignment 1


name = "John Smith"
age = 25
is_student = True

print('Name:' + name)
print('Age:' + str(age))
print('is_student: ' + str(is_student))

curr_year = 2023
birth_year = curr_year - age
print('Birth Year: ' + str(birth_year))

bio = name + ' is ' + str(age) + ' years old and is a student '
print(bio)

shopping_list = ['Fruit', 'Juice', 'Cheese']
print(shopping_list)
shopping_list.append('Chocolate')
print(shopping_list)

student_info = { 'Name' :'John Smith', 'Age' : 25, 'is_student' : True }
print(student_info)
print(student_info['Name'])
student_info['is_student'] = False
print(student_info)


