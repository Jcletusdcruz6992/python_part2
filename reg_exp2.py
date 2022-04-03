import re
def find_all(pattern,text):
    details=re.findall(pattern,text)
    print(details)

content='sa sd ssddd ssdsd ssssddd sdsdsss'
find='sd*'
find_all(find,content)
find='sd+'
find_all(find,content)
find='sd?'
find_all(find,content)
find='sd{3}'
find_all(find,content)
find='sd{1,3}'
find_all(find,content)
find='sd[sd]+'
find_all(find,content)
content="This is   a string!! and How can i help you!"
find='[^!.?]+'
find_all(find,content)
content="This is   a string!! and How can i help you!"
find='[a-z]+'
find_all(find,content)

content="This is   a string!! and How can i help you!"
find='[A-Z]+'
find_all(find,content)

content="This is   a string!! and How can i help you with 43765!"
find=r'\d+'
find_all(find,content)

content="This is   a string!! and How can i help you with 43765!"
find=r'\D+'
find_all(find,content)

#alpha numeric
content="This is   a string!! and How can i help you with 43765!"
find=r'\w+'
find_all(find,content)

content="This is   a string!! and How can i help you with 43765!"
find=r'\W+'
find_all(find,content)
