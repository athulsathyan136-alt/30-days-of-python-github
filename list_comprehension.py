code = 'Python'
lst = list(code)
print(lst)
print(type(lst))

print()

lst = [x for x in code]
print(lst)
print()

number = [num for num in range(11)]
print(number)
print()

a = [p*p for p in range(11)]
print(a)
print()

number = [(i,i*i) for i in range(11)]
print(number)
print()
even = [h for h in range(20) if h%2==0]
print(even)
print()

odd = [h for h in range(20) if h%2==1]
print(odd)
print()
numbers = [-8, -7, -3, -1, 0, 1, 3, 4, 5, 7, 6, 8, 10]
postive = [k for k in numbers if k%2 == 0 and k >0]
print(postive)
print()
list_of_lists = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
flat = [number for row in list_of_lists for number in row]
print(flat)
print()

def add_two(a,b):
    return a + b
print(add_two(2,3))
print()

add_two = lambda a,b:a + b
print(add_two(2,5))
print()

print((lambda a,b:a+b)(2,8))
print()
square = lambda x: x**2
print(square(3))
print()
mutli_variable = lambda a,b,c:a ** 2 - 3 * b + 4 * c
print(mutli_variable(5,5,3))
print()
def power(x):
    return lambda n: x**n
cube = power(2)(3)
print(cube)

print()
numbers = [-4, -3, -2, -1, 0, 2, 4, 6]
lst = [k for k in numbers if k <= 0 ]
print(lst)
print()
list_of_lists =[[1, 2, 3], [4, 5, 6], [7, 8, 9]]
num = [k for j in list_of_lists for k in j ]
print(num)
print()

y = [(i,1,i,i**2,i*3,i*4,i*5) for i in range(11)]
print(y)
countries = [[('Finland', 'Helsinki')], [('Sweden', 'Stockholm')], [('Norway', 'Oslo')]]
filters =[[j,j[:3],s ] for k in countries for j,s in k ]
print(filters)
print()
countries = [[('Finland', 'Helsinki')], [('Sweden', 'Stockholm')], [('Norway', 'Oslo')]]
dicts =[{'country':j,'city':f }for i in countries for j,f in i]
print(dicts)
print()
names = [[('Asabeneh', 'Yetayeh')], [('David', 'Smith')], [('Donald', 'Trump')], [('Bill', 'Gates')]]
name  = [i+' '+j for k in names for i,j in k]
print(name)
print()
slope= lambda m,x,c: m*x+c
print(f'slope:{slope(3,4,2)}')