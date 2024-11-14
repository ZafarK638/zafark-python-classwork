class Animal:
    def __init__(self,type,name,colour):
        self.myType = type
        self.myName = name
        self.myColour = colour
    #end of constructor method

    def eat(self):
        pass
    #end of function

    def makeNoise(self):
        pass
    #end of method

    def move(self):
        pass
    #end of method
#end of class




class Dog(Animal):
    def makeNoise(self,barkTimes):
        for _  in range(barkTimes):
            print("Woof!")
        # next _#end of class

class Cat(Animal):
    def makeNoise(self,meowTimes):
        for _  in range(meowTimes):
            print("Meow!")
#end of class


Pet = []

for i in ['cat','dog','cat','cat','dog']:
    match i:
        case 'cat':
            Pet.append(Cat("mammal","Name","Species"))
        case 'dog':
            Pet.append(Dog("mammal","Name","Species"))
        #end match
    #next animal


for i in Pet:
    i.makeNoise(1)
#next animal