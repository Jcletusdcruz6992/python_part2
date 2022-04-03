import one
def func():
    print('func running in two.py')
print('TOP level two.py')
if __name__ == '__main__':
    print('func() running directly in two.py')
else:
    print('two is being imported')
