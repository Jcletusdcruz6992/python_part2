import re
patterns=['This is a string with term1','term2']
text='This is a string with term1'
for pattern in patterns:
    print('My pattern is'+pattern)
    if re.search(pattern,text):
        print('There is a match')
    else:
        print('No match')
split_term='@'
email='jamescdcruz1995@gmail.com'
print(re.split(split_term,email))

print(re.findall('match','match is found match'))
