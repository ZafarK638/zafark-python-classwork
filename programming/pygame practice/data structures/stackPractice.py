class myStrStack:
    def __init__(self,size,front,back) -> None:
        self.sp = 1
        self.max = size
        self.data = ["" for _ in range(size)]
    #end constructor

    def isEmpty (self):
        return self.sp == -1
    #end method

    def isFull (self):
        return self.sp + 1 == self.max

    #end method

    def pushStack (self,item):
        if not self.isFull:
            self.sp += 1
            self.data[self.sp] = item
        else:
            print("Stack Full")
    #end method

    def popStack (self):
        if not self.isEmpty:
            poppedValue = self.data[self.sp]
            self.data[self.sp] = ""
            self.sp += -1
            return poppedValue
        else:
            print("Stack Empty")
    #end method

    def peekStack (self):
        if not self.isEmpty:
            return self.data[self.sp]
        else:
            print("Stack Empty")
    #end method
#end class
