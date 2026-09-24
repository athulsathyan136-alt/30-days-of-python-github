def add_two_numbers(num1,num2):
    return num1 + num2
print(f'Sum: {add_two_numbers(2,10)}')

def area_of_circle(r):
    return 3.14*r*r
z = area_of_circle(6)
print(f'Area of circle: {z}')

def add_all_nums(*nums):
    total = 0
    for i in nums:
        total+=i
    return total
print(add_all_nums(2,6,5,4,5,6))

def temp(temps):
     f = (temps*9/5)+32
     return f
print(f'C to F :{temp(22)}')

def check_seson(month):
    if month in ['jan','may']:
        return 








def calculate_slope(y2,y1,x2,x1):
    return (y2 - y1)/(x2 - x1)
print(calculate_slope(6,3,10,5))

def quadarctic(a,b,c,x = 2):
    return a*x**2 + b*x + c
print(quadarctic(a = 4,b = 5,c =6 ))


def print_list(*list):
    return [list,list,list]
print(print_list('anal','appu'))

def reverse_list(*array):
    return array[::-1]
print(reverse_list('a','b','c'))

def revers1(*numbers):
    box = []
    for i in range(len(numbers)-1,-1,-1):
        box.append(i)
    return box    
print(revers1(1,2,3,4,5,6))

def capitalize_list(*list):
    return [str(item).upper() for item in list]
print(capitalize_list('amal','athul'))

def add_item(lists,item):
    lists.append(item)
    return lists
food_stuff = ['Potato', 'Tomato', 'Mango', 'Milk']
print(add_item(food_stuff, 'Mango')) 
numbers = [2, 3, 7, 9]
print(add_item(numbers, 3))  

def remove_item(lists,items):
    if items in lists:
        lists.remove(items)
    return lists
food_stuff = ['Potato', 'Tomato', 'Mango', 'Milk']
print(remove_item(food_stuff, 'Mango'))  
numbers = [2, 3, 7, 9]
print(remove_item(numbers, 3))  

def sum_odd(numbers):
    return sum(i for i in range(1,numbers+1) if i%2!=0 )
print(sum_odd(5))

def sum_even(num):
    return sum(j for j in range(1,num - 1) if j%2==0 )
print(sum_even(6))

def even_and_odds(x):
    tot = 0
    to = 0
    for i in range(x+1):
        if i%2 == 0:
            tot+=1
        else:
            to+=1    
    return tot,to
print(even_and_odds(100))

def fact(n):
    if n == 0 or n ==1:
        return 1
    return n*fact(n-1)
print(fact(5))

def is_empty(para):
    return not para
print(is_empty([]))

def calculate_mean(data):
    if not data:
        return 0
    return sum(data) / len(data)

def median(data):
    if not data:
        return 0
    sort_data = sorted(sort_data)
    n = len(data)
    mid = n//2

def mode(data):
    if not data:
        return []
    freq = {}
    for num in data:
        freq[num] = freq.get(num,0) + 1
    max = max(freq.values())

def range(data):
    return max(data) - min(data)

def varience(data):
    n = len(data)
    if n < 2:
        return 0
    mean = calculate_mean(data)
    sq = sum((x - mean)** 2 for x in data)
    return sq / (n - 1 )

def std(data):
    if len(data) < 2:
        return 0 
    return varience(data) ** 0.5

if __name__ == "__main__":
    sample_list = [4, 8, 6, 5, 9, 4, 6, 6]

    print(f'{varience}')




def greet(name = 'Guest'):
    return f'Hello {name}!'
print(greet())
print(greet('Alice'))
  
def show_args(**kwargs):
    form = [f'{key} : {value}' for key,value in kwargs.items()]

    res = ','.join(form)

    print(f'Recevied : {res}')

show_args(name="Alice", age=30, city="New York")
# Received: name: Alice, age: 30, city: New York
show_args(name="Bob", pet="Fluffy, the bunny")
# Received: name: Bob, pet: Fluffy, the bunny  

def is_prime(num):
    if num < 1:
        return False
    for i in range(2,int(num**0.5)+1):
        if num%i==0:
            return  False
    return True   
def unique_list(lists):
    for i in set(lists):
        print(i)
uni = ['athul','athul','amal']
unique_list(uni)

def check_list(lists):
    return [type(item) for item in lists]
listtt = ['amal','athul']
print(check_list(listtt))

import keyword
def valid_variable(name):
    return name.isidentifier() and not keyword.iskeyword(name)
print(valid_variable('1user'))