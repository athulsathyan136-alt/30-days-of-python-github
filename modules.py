import random
import string
def random_user_id():
    chars = string.ascii_letters + string.digits
    return ''.join(random.choices(chars,k=6))
print(f'values: {random_user_id()}')    


import random
import string

def user_id_gen_by_user():
    num1 = int(input('Enter the each ID: '))
    num2 = int(input('Enter the number of id generated: '))

    chars =string.ascii_letters + string.digits

    for _ in range(num2):
        gene = ''.join(random.choices(chars,k=num1))
        print(gene)

user_id_gen_by_user()

import random

def rgb_color_gen():
    x = random.randint(3,255)
    y = random.randint(3,255)
    z = random.randint(3,255)

    return f'rgb({x},{y},{z})'

print(rgb_color_gen())

def list_of_hexa_colors():
    chars = string.digits + 'abcdef' 

    return '#'+''.join(random.choices(chars , k =6))
print(list_of_hexa_colors())

def generate_colors(hex,num):
    count = []
    if hex.lower() == 'hexa':
        chars = string.digits + 'abcdef' 
        for _ in range(num):
            hexs = '#'+''.join(random.choices(chars,k = 6))
            count.append(hexs)
    elif hex.lower() == 'rgb':
        x = random.randint(3,255)
        y = random.randint(3,255)
        z = random.randint(3,255)
        rgb = f'rgb({x},{y},{z})'      
        count.append(rgb) 
    else:
        return 'invalid'

    return count
print("Hexa Colors:", generate_colors("hexa", 3))
           

def shuffle_list(lists):
    random.shuffle(lists)
    return lists
print(shuffle_list([1,2,3,4]))

def arrays():
    result = random.sample(range(0,10),7)
    return result
print(arrays())

           