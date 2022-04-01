try:
    f=open('simple.txt','w')
    f.write('Hi,am James')
except IOError:
    print("Error,could not open file!")
else:
    print('Success')
finally:
    print('I always work,no matter what!')
