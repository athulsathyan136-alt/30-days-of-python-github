# sets
it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
age = [22, 19, 24, 25, 26, 24, 25, 24]
print(f"length of it_companies: {len(it_companies)}")
it_companies.add('Twitter')
print(f'New : {it_companies}')
it_companies.update(['Meta','MI','TCS'])
print(f'After added 3 new company: {it_companies}')
it_companies.remove('MI')
print(f'After removing MI :{it_companies}')

print('EXERCISES 2')

set1 = A.union(B)
print(f'A join B : {set1}')
set2 = A.intersection(B)
print(f'A intersection B : {set2}')
print(f"is A subset of B {A.issubset(B)}")
print(f'Are A and B disjoint sets :{A.isdisjoint(B)}')

jo = A.union(B)
ji = B.union(A)
print(f'A join B : {jo}')
print(f'B join A : {ji}')

print(f'Clear the set : {A.clear()}')
print(f'Clear the set : {B.clear()}')

print("EXERCISES 3")

ages = set(age)
print(ages)
print(f'Length of the list: {len(ages)}')
print(f'max: {max(ages)}')

word = "I am a teacher and I love to inspire and teach people. "
wo = word.replace(".",'').split()
print(set(wo))
print(len(wo))