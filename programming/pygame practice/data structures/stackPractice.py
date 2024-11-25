class myStrStack:
    def __init__(self,size) -> None:
        self.sp = 1
        self.max = size
        self.data = ["" for _ in range(size)]
    #end constructor

    def isEmpty (self) -> bool:
        return self.sp == -1
    #end method

    def isFull (self) -> bool:
        return self.sp + 1 == self.max

    #end method

    def pushStack (self,item) -> None:
        if not self.isFull:
            self.sp += 1
            self.data[self.sp] = item
        else:
            print("Stack Full")
    #end method

    def popStack (self) -> None:
        if not self.isEmpty:
            self.data[self.sp] = ""
            self.sp += -1
            return self.data[self.sp + 1]
        else:
            print("Stack Empty")
    #end method

    def peekStack (self) -> None:
        if not self.isEmpty:
            return self.data[self.sp]
        else:
            print("Stack Empty")
    #end method
#end class

len_stack = int(input("Input an integer: "))
stack1 = myStrStack(len_stack)