def line(files):
    line = 0
    word = 0
    for file in files:
        with open(file,'r') as file_name:
            reader = file_name.readlines()
            for read in reader:
                line+=1
                word += len(read.split())
            print(f'Number of line: {line}')
            print(f'Number of words : {word}')

file1 = 'Obama_speech.txt'
file2 = 'melina_trump_speech.txt'
file3 = 'michelle_obama_speech.txt'
file4 = 'donald_speech.txt'
files = [file1,file2,file3,file4]

line(files)


print()
import os
import json
from collections import Counter 
def top_ten(filename,top_ten):
    number = 0
    with open(filename ,'r',encoding='utf-8') as files:
        data = json.load(files)
        all = []
        for country in data:
            if 'languages' in country:
                all.extend(country['languages'])
        lan_count = Counter(all)
        most = lan_count.most_common(top_ten)
        form_1 = [(count, langs) for langs, count in most]
        return form_1
script_dir = os.path.dirname(os.path.abspath(__file__))

# 2. Build the correct path to your JSON file (try both possible structures)
path_option_1 = os.path.join(script_dir, 'data', 'countries_data.json')
path_option_2 = os.path.join(script_dir, 'countries_data.json')

# 3. Choose the path that actually exists on your computer
target_file = path_option_1 if os.path.exists(path_option_1) else path_option_2

# 4. Pass the guaranteed path into your function
print(top_ten(target_file, 10))

import json
from collections import Counter
import re
def find_most(filename,top=10):
    with open(filename ,'r',encoding='utf-8') as file:
        text = file.read().lower()

        words = re.findall(r'\b[a-z]+\b',text)

        word_count = Counter(words)

        most = word_count.most_common(top)

        fromat = [(count,word) for word, count in most]
        return fromat
print(find_most('romeo_and_juliet.txt', 10))
    