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

    def change_colour(self,diff_col):
        self.colour = diff_col
    #end of method

    def change_name(self,diff_name):
        self.name = diff_name
    #end of method
#end of class

my_cat = Cat("Antonio Banderas","Orange")
my_cat.meow(2)
print(my_cat.name)
my_cat.meow(3)
my_cat.change_colour(str(input()))
my_cat.change_name(str(input()))
print(my_cat.colour,my_cat.name)