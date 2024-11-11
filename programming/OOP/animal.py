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

myAnimal = Animal("Unknown","Rizzly Bear","Neon Green")
print(f"Type: {myAnimal.myType} Name: {myAnimal.myName} Colour: {myAnimal.myColour}")
myAnimal.makeNoise


class Dog(Animal):
    pass
#end of class

myDog = Dog("MurderKing","Anthropomorphic hybrid", "Bright Yellow")
print(f"Type: {myDog.myType} Name: {myDog.myName} Colour: {myDog.myColour}")
print("End")
