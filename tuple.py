tp = ()
bro = ('Arun','Varun')
sis = ('paru','midhu')
total = bro+sis
print('Sibilings: ',total)
print("Number of Sibilings: ",len(total))
bro = ('Arun','Varun','sath','Nayana')
family=bro
print('My family: ',family)

bro = ('Arun','Varun','sath','Nayana')
a,b,c,d = bro
print(a)
print(b)
print(c)
print(d)

fruits = ('apple','orange','mango','lemon')
veg = ('carrot','onion','ladyfinger')
animal = ('cat','dog','parrot')
food_stuff_tp = fruits+veg+animal
print("All : ",food_stuff_tp)
food_stuff_lt = food_stuff_tp
food_slic = len(food_stuff_tp)//2
food = food_stuff_tp[food_slic]
print(food)
first_3 = food_stuff_tp[0:3]
print('Fisrt 3:',first_3)
last = food_stuff_tp[-3:]
print("Last 3 :",last)

nordic_countries = ('Denmark', 'Finland','Iceland', 'Norway', 'Sweden')
print("Check if 'Estonia' is a nordic countr")
print('Estonia' in nordic_countries)
print("Check if 'Iceland' is a nordic country")
print('Iceland' in nordic_countries)
