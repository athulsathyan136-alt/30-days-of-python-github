import webbrowser # web browser module to open websites

# list of urls: python
url_lists = [
    'http://www.python.org',
    'https://www.linkedin.com/in/asabeneh/',
    'https://github.com/Asabeneh',
    'https://twitter.com/Asabeneh',
]

# opens the above list of websites in a different tab
for url in url_lists:
    webbrowser.open_new_tab(url)


import requests

url = 'https://www.w3.org/TR/PNG/iso_8859-1.txt'

response = requests.get(url)
print(response)
print(response.status_code)
print(response.headers)
print(response.text)


import requests
from collections import Counter
import re
url = 'http://www.gutenberg.org/files/1112/1112.txt'
response = requests.get(url)
text = response.text
word = re.findall(r'\b\w+\b',text.lower())
word_count = Counter(word)
for word,count in word_count.most_common(20):
    print(f'{word}:{count}')

import requests
import statistics
urls = 'https://api.thecatapi.com/v1/breeds' 

response = requests.get(urls)

texts = response.json()

life = []
for breed in texts:
    if 'life_span' in breed:
        low,high = map(int,breed['life_span'].replace('',',').split('-'))
        avg = low+high/2
        life.append(avg)

min_life = min(life)
max_life = max(life)
mean_life = statistics.mean(life)
median_life = statistics.median(life)

print(f"Minimum Life Span: {min_life} years")
print(f"Maximum Life Span: {max_life} years")
print(f"Mean Life Span: {mean_life:.2f} years")
print(f"Median Life Span: {median_life} years")

print()

url = 'https://api.thecatapi.com/v1/breeds'

response = requests.get(url)

breeds = response.json()

country = []
for countrys in country:
    origin = countrys.get('origin')
    if origin:
        country.append(origin)

counter = Counter(country)

print(f'{'country':<25} | {'number of Breed':<15}')
print('='*40)
for counta, count in counter.most_common():
    print(f'{counta<25} | {count:<15}')

import pandas as pd
from ucimlrepo import fetch_ucirepo

iris = fetch_ucirepo(id=53)

x = iris.data.features
y =iris.data.targets

print(x.head())
print(y.head())

print(f'\n Dataset description:{iris.metadata.name}')
print(f'Total instance {iris.metadata.num_instances}')