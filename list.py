lst = []
fruits = ['apple','orange','melon','banana','kiwi']
print('Length: ',len(fruits))
print(fruits[0])
print(fruits[1])
print(fruits[-1])

address = ['Athul','25','7.5','single','Thaipparambil']
it_address =['Facebook','Google','Microsoft','Apple','IBM','Oracle','Amazon']
print(address)
print(it_address)

print('length of it companies: ',len(it_address))
print('First :',it_address[0])
print('Middle :',it_address[3])
print('Last :',it_address[-1])

it_address.append('Meta')
print(it_address)
it_address.insert(3,'ZOHO')
print(it_address)
print(it_address[1].upper())
print(' # '.join(it_address))
it =  ['IBM','Meta'] in it_address
print(it)
it_fied = sorted(it_address)
print(it_fied)
it_address.reverse()
print(it_address)
print(it_address[0:3])
print(it_address[-3:])
print(it_address[4])
print(it_address.pop(0))
print(it_address.pop(4))
print(it_address.pop(-1))
it_address.clear() 
print(it_address)

front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
back_end = ['Node','Express', 'MongoDB']
full = front_end+back_end
print(full)
full_stack = full.copy()
full_stack.insert(5,'Python')
full_stack.insert(6,'SQL')
print(full_stack)

ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]
print(ages)
ages.sort()
print('Sorted: ',ages)
print('min:',min(ages))
print('max:',max(ages))
print('Sum:',min(ages)+max(ages))
print('Median Age: ',sum(ages)/len(ages))
print('Average: ',sum(ages)/len(ages))
print('Range :',max(ages)-min(ages))
hh = sum(ages)/len(ages)
print('Max value: ',abs(max(ages)-hh))
print('Min value : ',abs(min(ages)-hh))

countries = [
  'Afghanistan',
  'Albania',
  'Algeria',
  'Andorra',
  'Angola',
  'Antigua and Barbuda',
  'Argentina',
  'Armenia',
  'Australia',
  'Austria',
  'Azerbaijan',
  'Bahamas',
  'Bahrain',
  'Bangladesh',
  'Barbados',
  'Belarus',
  'Belgium',
  'Belize',
  'Benin',
  'Bhutan',
  'Bolivia',
  'Bosnia and Herzegovina',
  'Botswana',
  'Brazil',
  'Brunei',
  'Bulgaria',
  'Burkina Faso',
  'Burundi',
  'Cabo Verde',
  'Cambodia',
  'Cameroon',
  'Canada',
  'Central African Republic',
  'Chad',
  'Chile',
  'China',
  'Colombia',
  'Comoros',
  'Congo, Democratic Republic of the',
  'Congo, Republic of the',
  'Costa Rica',
  "Côte d'Ivoire",
  'Croatia',
  'Cuba',
  'Cyprus',
  'Czech Republic',
  'Denmark',
  'Djibouti',
  'Dominica',
  'Dominican Republic',
  'East Timor (Timor-Leste)',
  'Ecuador',
  'Egypt',
  'El Salvador',
  'Equatorial Guinea',
  'Eritrea',
  'Estonia',
  'Eswatini',
  'Ethiopia',
  'Fiji',
  'Finland',
  'France',
  'Gabon',
  'Gambia',
  'Georgia',
  'Germany',
  'Ghana',
  'Greece',
  'Grenada',
  'Guatemala',
  'Guinea',
  'Guinea-Bissau',
  'Guyana',
  'Haiti',
  'Honduras',
  'Hungary',
  'Iceland',
  'India',
  'Indonesia',
  'Iran',
  'Iraq',
  'Ireland',
  'Israel',
  'Italy',
  'Jamaica',
  'Japan',
  'Jordan',
  'Kazakhstan',
  'Kenya',
  'Kiribati',
  'Korea, North',
  'Korea, South',
  'Kuwait',
  'Kyrgyzstan',
  'Laos',
  'Latvia',
  'Lebanon',
  'Lesotho',
  'Liberia',
  'Libya',
  'Liechtenstein',
  'Lithuania',
  'Luxembourg',
  'Madagascar',
  'Malawi',
  'Malaysia',
  'Maldives',
  'Mali',
  'Malta',
  'Marshall Islands',
  'Mauritania',
  'Mauritius',
  'Mexico',
  'Micronesia',
  'Moldova',
  'Monaco',
  'Mongolia',
  'Montenegro',
  'Morocco',
  'Mozambique',
  'Myanmar',
  'Namibia',
  'Nauru',
  'Nepal',
  'Netherlands',
  'New Zealand',
  'Nicaragua',
  'Niger',
  'Nigeria',
  'North Macedonia',
  'Norway',
  'Oman',
  'Pakistan',
  'Palau',
  'Palestine',
  'Panama',
  'Papua New Guinea',
  'Paraguay',
  'Peru',
  'Philippines',
  'Poland',
  'Portugal',
  'Qatar',
  'Romania',
  'Russia',
  'Rwanda',
  'Saint Kitts and Nevis',
  'Saint Lucia',
  'Saint Vincent and the Grenadines',
  'Samoa',
  'San Marino',
  'Sao Tome and Principe',
  'Saudi Arabia',
  'Senegal',
  'Serbia',
  'Seychelles',
  'Sierra Leone',
  'Singapore',
  'Slovakia',
  'Slovenia',
  'Solomon Islands',
  'Somalia',
  'South Africa',
  'South Sudan',
  'Spain',
  'Sri Lanka',
  'Sudan',
  'Suriname',
  'Sweden',
  'Switzerland',
  'Syria',
  'Tajikistan',
  'Tanzania',
  'Thailand',
  'Togo',
  'Tonga',
  'Trinidad and Tobago',
  'Tunisia',
  'Turkey',
  'Turkmenistan',
  'Tuvalu',
  'Uganda',
  'Ukraine',
  'United Arab Emirates',
  'United Kingdom',
  'United States',
  'Uruguay',
  'Uzbekistan',
  'Vanuatu',
  'Vatican City',
  'Venezuela',
  'Vietnam',
  'Yemen',
  'Zambia',
  'Zimbabwe'
]

id = len(countries)//2
id2 = countries[id]
print(id2)
first = countries[0:98]
print('First half:',first)
second = countries[99:]
print('secon half: ',second)
print()
countries_even = ['India', 'Japan', 'Brazil', 'Germany', 'Canada', 'Egypt']
mid = len(countries_even)//2
first1,sec = countries_even[:mid],countries_even[mid:]
print(first1)
print(sec)
print()
countries_odd = ['India', 'Japan', 'Brazil', 'Germany', 'Canada', 'Egypt','Mexico']
mid = len(countries_odd)//2
nfirst1,nsec = countries_odd[:mid],countries_odd[mid:]
print(nfirst1)
print(nsec)