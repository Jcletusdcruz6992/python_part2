class Sample():
    pass
x=Sample()
print(type(x))

class Dog():
    #class object attribute
    species="mammal"
    def __init__(self,breed,name):
        self.breed=breed
        self.name=name
mydog=Dog('lambo','Ricky')
otherdog=Dog('huskie','Johnny')
print(mydog.breed)
print(mydog.name)
print(mydog.species)
print(otherdog.breed)
print(otherdog.name)
print(otherdog.species)



class Circle():
    pi=3.14
    def __init__(self,radius=1):
        self.radius=radius
    def area(self):
        return self.radius*self.radius*Circle.pi
mycir=Circle(3)
print(mycir.radius)
print(mycir.area())
