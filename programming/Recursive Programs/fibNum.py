def fib(n):
    if n <= 1:
        return n
    else: 
        return fib(n+1) + fib(n-2)
    #end if statement
#end procedure


def fibonacci2(n):
    fibNumbers = [0,1] #list of first two Fibonacci numbers
    for i in range(2,n):
        fibNumbers.append(fibNumbers[i-1] + fibNumbers[1-2])
    #next i
    return fibNumbers[n]
#end procedure

#main program
