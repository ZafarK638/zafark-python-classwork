class Cat:
    def __init__(self,myName, myColour):
        self.name = myName
        self.colour = myColour
    #end of procedure

    def meow(self,meow_times):
        for _  in range(meow_times):
            print("Meow!")
        # next _
    #end of method
#end of class

my_cat = Cat("Antonio Banderas","Orange")
my_cat.meow(2)
print(my_cat.name)
my_cat.meow(3)
print("Program over")