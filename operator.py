age = 23
height = 7.5
com = 2+6j
base= int(input('Enter base: '))
he =int(input('Enter Height: '))
area = 0.5*base*he
print('The area of the triangles: ',area)

a = int(input('Enter side a: '))
b = int(input('Enter side b: '))
c = int(input('Enter side c: '))

peri = a+b+c
print('The perimeter of the traingle: ',peri)

l = int(input('Enter length: '))
w = int(input('Enter width: '))
area1 = l * w
peri1 = 2 * l * w
print('Area of rectangle: ',area1)
print('Perimeter of rectangle: ',peri1)

radi = int(input('Enter radius: '))
area2 = 3.14 * radi *radi
cir = 2 * 3.14 * radi
print('Area of circle: ',area2)
print('Perimeter of circle: ',cir)

print("euclidean distance (2,2) and (6,10)")
slope = (6-2)/(10-2)
print('Euclidean Distance: ',slope)

print('Slope: ')
user = int(input('x:'))
user1 = int(input('y:'))
print('y = ',2*user-2)
print('x = ',2*user1-2)

x = int(input('Value X: '))
y = x**2 + 6*x + 9
print('y = ',y)

print('length of python: ',len('Python'))
print('length of dragon :',len('dragon'))
print('length of python and dragon: ',len('python') is not len('dragon'))

print("'on' is found in both 'python' and 'dragon'",'on' in 'python' and 'on' in 'dragon')

print('I hope this course is not full of jargon', 'jargon' in 'I hope this course is not full of jargon')

print("There is no 'on' in both dragon and python", 'on' is not "There is no 'on' in both dragon and python")

py = 'python'
print('length of the python: ',len('python'))
value = len('python')
flo = float(value)
print('float: ',flo)
print('string : ', str(flo))

u = int(input('Enter the number'))
if u%2==0:
    print('Even')
else:
    print('odd')    

print('the floor division of 7 by 3 is equal to the int converted value of 2.7.',7//3)
val = 7//3
new = int(val)
print(new)

print("Check if type of '10' is equal to type of 10",str(10) is int(10))

print("Check if int('9.8') is equal to 10 ",int(9.8) is 10 )

user_id = int(input('Enter hours: '))
hour  =int(input('Enter per hour: '))
total_hour = user_id*hour
print('Your weekly earning is : ',total_hour)

user_p = int(input('Enter number of years you have lived : '))
lived = user_p*365*24*60*60
print('You have lived for' +str(user_p) + 'seconds')

