dog = {}
dog['name'] = 'Luna'
dog['color'] = 'white'
dog['breed'] = 'pug' 
dog['legs'] = 4
dog['age'] = 5

print(f'Dogs : {dog}')

student = {'first_name': 'Milan','last_name': 'Benny','gender':'M','age':25,'marital status':'single','skills':['agri','reading'],'city':'upputhara','address':'milanpbennyHouse'}
print(f'Length of students: {len(student)}')
print(f'skills :{student["skills"]}')
print(type(student['skills']))
student['skills'].append('book')
print(f'skills :{student["skills"]}')
print()
key = student.keys()
print(f'keys :{key}')
print()
value = student.values()
print(f'values :{value}')
print()
di = student.items()
print(di)
student.pop('age')
print(f'new list: {student}')
stu = student.popitem()
print(f'Deleted item: {stu}')