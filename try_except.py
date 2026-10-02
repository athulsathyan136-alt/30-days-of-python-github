try:
    print(10 + '5')
except:
    print('Something went wrong!')

try:
    name = input('Enter the name: ')
    year = input('Enter the year')
    age = 2019 - year
    print(f"You are {name} .And age is{age}")
except:
    print('Something went wrong!')


try:
    name = input('enter the name:')
    year = input('enter the year: ')
    age = year - 2019
    print(f"You name is {name} .And your age {age}")
except TypeError:
    print('Type error occured')
except ValueError:
    print('Value error occured')
except ZeroDivisionError:
    print('zero division error occured')

try:
    name = input('enter the name:')
    year = input('enter the year: ')
    age = int(year) - 2019
    print(f"You name is {name} .And your age {age}")
except TypeError:
    print('Type error occured')
except ValueError:
    print('Value error occured')
except ZeroDivisionError:
    print('zero division error occured')
else:
    print('i usually run with the try block!')
finally:
    print('XXX-NO error-XXX')

try:
    name = input('enter the name:')
    year = input('enter the year: ')
    age = year - 2019
    print(f"You name is {name} .And your age {age}")
except Exception as e:
    print(e)


def sum(a,b,c,d,e):
    return a+b+c+d+e
lists = [1,2,3,4,5] 
print(sum(*lists))

countries = ['Finland', 'Sweden', 'Norway', 'Denmark', 'Iceland']
fin,swe,nor,*others = countries
print(fin,swe,nor,others)

numbers = [1, 2, 3, 4, 5, 6, 7]
first ,*middle,last = numbers
print(first,middle,last)

def unpack(name,country,city,age):
    return f"{name} lives in {country} ,{city} .He is {age} year old"
dct = {'name':'Asabeneh', 'country':'Finland', 'city':'Helsinki', 'age':250}
print(unpack(**dct))

def summ(*args):
    s = 0
    for i in args:
        s+=1
    return s
print(summ(1,2,3))
print(summ(1,2,3,5,6,4,5,6,5,))

def kwags(**k):
    for key in k:
        print(f"{key} = {k[key]}")
    return k
print(kwags(name="Asabeneh",
      country="Finland", city="Helsinki", age=250))

lst_one = [1, 2, 3]
lst_two = [4, 5, 6, 7]
lst = [0,*lst_one,*lst_two]
print(lst)

for index , item in enumerate([20,30,40]):
    print(index,item)

fruits = ['banana', 'orange', 'mango', 'lemon', 'lime']                    
vegetables = ['Tomato', 'Potato', 'Cabbage','Onion', 'Carrot']
new = []
for lst , v in zip(fruits,vegetables):
    new.append({'fruit':lst,'veg':v})
print(new)

names = ['Finland', 'Sweden', 'Norway','Denmark','Iceland', 'Estonia','Russia']
f,s,n,d,i,*es = names
print(f,s,n,d,i,es)