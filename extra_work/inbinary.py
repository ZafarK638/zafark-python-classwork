def toBinary(num):
    binary = ""
    while num != 0:
        if num%2 == 0:
            binary += "1"
            num = num/2
        else:
            binary += "0"
            num = (num-1)/2
        #end if else statement
    #end while statement
    return binary
#end function

x = int(input("Input a number: "))
print(toBinary(x))