class Animal():
    def __init__(self):
        print('Animal Created')
    def whoAmI(self):
        print('Animal')
    def eat(self):
        print('Eating')
mya=Animal()
mya.whoAmI()
mya.eat()

class Dog(Animal):
    def __init__(self):
        Animal.__init__(self)
        print('Dog Created')
    def bark(self):
        print('woo')
    def eat(self):
        print('Dog is Eating')
mydog=Dog()
mydog.whoAmI()
mydog.eat()
mydog.bark()
