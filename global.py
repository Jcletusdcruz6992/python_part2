x=25

def my_fun():
    x=2
    return x

print(x)
print(my_fun())

name='This is global name'
def boom():
    name='Sammy'
    def hello():
        print('Hello'+name)
    hello()
boom()
print(name)

y=50

def my_funs(y):
    print('Value of y:',y)
    y=60
    print('Value of y:',y)
my_funs(y)
print(y)
