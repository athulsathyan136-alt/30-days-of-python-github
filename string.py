t = 'Thirty'
y = 'Days'
u = 'Of'
i = 'Python'
print(t+y+u+i)

a = 'Coding'
b = 'For'
c = 'All' 
print(a+b+c)
company = 'Coding For All'
print(company)
print(len(company))
print(company.lower())
print(company.upper())
print(company.title())
print(company.capitalize())
print(company.swapcase())
si = company[0:6] 
print(si)
sub = 'Coding'
print(company.index(sub))
print(company.find('Coding'))
re = company.replace('Coding For All','Python')
print(company)
print(re)
p = "Python for Everyone"
p1 = p.replace("Python for Everyone","Python for All")
print(p)
print(p1)
spli = company.split(' ')
print(spli)
com = "Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon".split(',')
print(com)
print(company[0])
print(company[-1])
print(company[10])
f = 'Python For Everyone'
print(f[0],end='')
print(f[7],end='')
print(f[11],end='\n')
f = 'Coding For All'
print(f[0],end='')
print(f[7],end='')
print(f[11],end='\n')

print(f.index('C'))
print(f.index('F'))
print(f.rfind('l'))

sent = 'You cannot end a sentence with because because because is a conjunction'
print(sent.find('because'))
print(sent.index('because'))
print(sent.rfind('because'))


x = 'You cannot end a sentence with because because because is a conjunction'
z = x.find('because')
print(z)

y = x[31:55]
print(y)

print(company.startswith('Coding?'))
print(company.endswith('Coding?'))

p = '   Coding For All      ' 
print(p)
print(p.strip())

f1 = '30DaysOfPython'
f2 = f1.isidentifier()
print(f2)

f3 = 'thirty_days_of_python'
f4 = f3.isidentifier()
print(f4)

f5 = ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']
f6 = ''.join(f5)
print(f6)







g = 'Name\tAge\tCountry\tCity'
j = 'Asabeneh\t250\tFinland\tHelsinki'

print(g.expandtabs(8))
print(j.expandtabs(7))

radius = 10
area = 3.14 * radius ** 2
print('The area of a circle with radius {} is {} meters square'.format(radius,area))

k = 8
l = 6

print('%d + %d = '%(k,l),k+l )
print('%d - %d = '%(k,l),k-l )
print('%d * %d = '%(k,l),k*l )
print('%d / %d = '%(k,l),k/l )
print("%d %% %d = "%(k,l),k%l )
print('%d // %d = '%(k,l),k//l )
print('%d ** %d = '%(k,l),k**l )