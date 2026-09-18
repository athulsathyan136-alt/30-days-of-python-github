user = int(input('Enter your age: '))
if user >=18:
    print('You are old enough to learn to drive')
elif user < 18:
    us = 18 - user
    print(f'You need {us} more years to learn to drive')

age = int(input('Enter your age'))
my_age = 5
if age == my_age:
    print('same age')
else:    
    if age > my_age:
        age_diff = age - my_age
        if age_diff ==1:
            print(f'i am older than you {age_diff} year')
        else:
             print(f'i am older than you {age_diff}  years') 
    else:
        age_diff = my_age - age
        if age_diff == 1:
            print(f'you are older than me {age_diff} year')
        else:
            print(f'you are older than me {age_diff} years')   


num  = int(input('Enter number one: '))
num2 = int(input('Enter number two: '))
if num > num2:
    print(f'{num} is greater than {num2}')
elif num < num2:
    print(f'{num} is less than {num2}')
else:
    print(f'{num} is equal to {num2}')


score = int(input('Enter the Marks: '))
if 90 <= score <=100:
    print('A')
elif 80 <= score <90:
    print('B')
elif 70 <= score <80:                   
    print('C')
elif 60 <= score <70:
    print('D')
else:
    print('F')        

season  = input('Enter the season: ').title()
if season in ['September', 'October', 'November']:
    print('Season : AUTUMN')
elif season in ['December', 'January', 'February']:  
    print('Season : WINTER')
elif season in ['March', 'April', 'May']:
    print('Season: SPRING')
elif season in ['June', 'July', 'August']:
    print('Season : SUMMER')
else:
    print('Invakid month')    
        
fruits = ['banana', 'orange', 'mango', 'lemon']
inputs = input('Enter fruit: ')
if inputs in fruits:
    print('Already in the fruits lists')
else:
    fruits.append(inputs)
    print(f'Modified list: {fruits}')    

person={
    'first_name': 'Asabeneh',
    'last_name': 'Yetayeh',
    'age': 250,
    'country': 'Finland',
    'is_married': True,
    'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address': {
        'street': 'Space street',
        'zipcode': '02210'
    }
    }

if 'skills' in person:
    middle = len(person['skills'])//2
    print(f'Middle skills list :{person['skills'][middle]}')
if 'skills' in person:
    python_1 = 'Python' in person['skills']
    print(f'has python skills: {python_1}')
if 'skills' in person:
    skill = person['skills']    
    if  'JavaScript' in skill and 'React' in skill:
        print('He is a front end developer')
    elif 'Node' in skill and 'Python' in skill and 'MangoDB' in skill:
        print('He is a backend developer')    
    elif 'React' in skill and 'Node' in skill and 'MangoDB' in skill:
        print('He is a fullstack developer')  
    else:
         print('unknown title')       

if person['is_married'] and person['country'] == 'Finland':
    print(f'{person['first_name']} {person['last_name']} lives in {person['country']}. He is married')
