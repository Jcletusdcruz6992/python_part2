def func():
    print('func() in one.py is running ')
print('Top level one.py')
if __name__ == '__main__':
    print('one.py is running directly ')
else:
    print('one.py has been imported')
