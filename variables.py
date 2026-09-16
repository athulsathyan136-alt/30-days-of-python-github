#Day 2:30 Days of python programming
first_name = 'Athul'
last_name = 'sathyan'
full_name = 'Athul Sathyan'
country = 'india'
city = 'kattapana'
age = 23
year = 2003
is_marriage = 'No'
is_true = True
is_light = 'On'
num1,num2,num3 = 10,20,30

print(type(first_name))
print(type(last_name))
print(type(full_name))
print(type(country))
print(type(age))
print(type(year))
print(type(is_marriage))
print(type(is_true))
print(type(is_light))
print(type(num1))
print(type(num2))
print(type(num3))

print('first name length:',len(first_name))
print('last name length:',len(last_name))

num_one = 5
num_two = 4
total = num_one+num_two
diff = num_two - num_one
product = num_two*num_one
division = num_one / num_two
remainder = num_one // num_two
exp = num_one**num_two
floor_division = num_one/num_two
radius = int(input("Radius: "))
area =  3.14 * radius
cir = 2 * 3.14 * radius
print(f'Circle Area: {area}')
print(f'Circumference : {cir}')

first = input('Enter Your First name: ').title()
Last = input('Enter Your Last name: ').title()

print(f'Full Name: {first} {Last}')

help('keywords')