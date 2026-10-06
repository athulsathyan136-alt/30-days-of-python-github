import re
from collections import Counter
txt = 'I love to teach python and javaScript'
match = re.match('I love to teach',txt,re.I)
print(match)
span = match.span()
print(span)
start,end = span
print(start,end)
substring = txt[start:end]
print(substring)
print()
txt = 'I love to teach python and javaScript'
match = re.match('I like to teach', txt, re.I)
print(match)  

txt = '''Python is the most beautiful language that a human being has ever created.
I recommend python for a first programming language'''

match = re.search('first',txt,re.I)
print(match)
span = match.span()
print(span)
start,end = span
print(start,end)
substring = txt[start:end]
print(substring)
print()
txt = '''Python is the most beautiful language that a human being has ever created.
I recommend python for a first programming language'''

matches = re.findall('language',txt,re.I)
print(matches)
print()

txt = '''Python is the most beautiful language that a human being has ever created.
I recommend python for a first programming language'''
match_replace = re.sub('Python|python','JavaScript',txt,re.I)
print(match_replace)
print()
txt = '''%I a%m te%%a%%che%r% a%n%d %% I l%o%ve te%ach%ing.
T%he%re i%s n%o%th%ing as r%ewarding a%s e%duc%at%i%ng a%n%d e%m%p%ow%er%ing p%e%o%ple.
I fo%und te%a%ching m%ore i%n%t%er%%es%ting t%h%an any other %jobs.
D%o%es thi%s m%ot%iv%a%te %y%o%u to b%e a t%e%a%cher?'''

match_re = re.sub('%','',txt)
print(match_re)

print()
txt = '''I am teacher and  I love teaching.
There is nothing as rewarding as educating and empowering people.
I found teaching more interesting than any other jobs.
Does this motivate you to be a teacher?'''
print(re.split('\n',txt))

print()
regex = r'[Aa]pple'
txt= 'Apple and banana are fruits. An old cliche says an apple a day a doctor way has been replaced by a banana a day keeps the doctor far far away.'
matches = re.findall(regex,txt)
print(matches)

regex_pattern = r'\d'  # d is a special character which means digits
txt = 'This regular expression example was made on December 6,  2019 and revised on July 8, 2021'
matches = re.findall(regex_pattern, txt)
print(matches)  # ['6', '2', '0', '1', '9', '8', '2', '0', '2', '1'], this is not what we want

regex = r'\d+'
txt = 'This regular expression example was made on December 6,  2019 and revised on July 8, 2021'
matches = re.findall(regex,txt)
print(matches)
txt = 'This regular expression example was made on December 6,  2019 and revised on July 8, 2021'
regex_pattern = r'^This'  # ^ means starts with
matches = re.findall(regex_pattern, txt)
print(matches) 
txt = 'This regular expression example was made on December 6,  2019 and revised on July 8, 2021'
matches = re.findall(r'[^A-Za-z ]+',txt)
print(matches)
print()

paragraph = 'I love teaching. If you do not love teaching what else can you love. I love Python if you do not love something which can give you all the capabilities to develop an application what else can you love.'
matches = re.findall(r'\b\w+\b',paragraph.lower())
word = Counter(matches)
most,count = word.most_common(1)[0]
print(f'Most frequent:{most} {count}')
print()

txt = 'The position of some particles on the horizontal x-axis are -12, -4, -3 and -1 in the negative direction, 0 at origin, 4 and 8 in the positive direction. Extract these numbers from this whole text and find the distance between the two furthest particles.'

matches = re.findall(r'-?\d+',txt)
print('points',matches)
sorted = sorted([int(x) for x in matches])
print(sorted)

distance = sorted[-1] - sorted[0]
print(distance)



def isvalid(variable):
    txt = r'^[a-zA-Z_]\w*$'
    if re.match(txt,variable):
        return True
    return False

print(isvalid('first_name')) 
print(isvalid('first-name')) 
print(isvalid('1first_name')) 
print(isvalid('firstname')) 


def clean_text(sentence):
    txt = re.sub(r'[^\w\s]','',sentence)
    word = txt.lower().split()
    count = Counter(word)
    return count
sentence = '''%I $am@% a %tea@cher%, &and& I lo%#ve %tea@ching%;. There $is nothing; &as& mo@re rewarding as educa@ting &and& @emp%o@wering peo@ple. ;I found tea@ching m%o@re interesting tha@n any other %jo@bs. %Do@es thi%s mo@tivate yo@u to be a tea@cher!?'''
words = clean_text(sentence)
print(words)
