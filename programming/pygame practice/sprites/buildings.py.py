class Building:
    def __init__(self,pHeight,pWidth,pFloors) -> None:
        self.__height = pHeight #private
        self.__width = pWidth #private
        self.__floors = pFloors #private
    #end constructor (new)
    
    def getNumberFloors(self):
        return self.__floors
    #end method

    def setNumberFloors(self,newFloor):
        if newFloor >= 1:
            self.__floors = newFloor
            return True
        else:
            return False
        #end if-else statement
    #end method
#end class