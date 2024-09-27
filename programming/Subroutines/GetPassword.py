def getPword(attempt):
    if attempt == 1:
        print("Please enter a password between 6 and 8 characters: ")
        Pword = str(input())
    #endif
    if attempt == 2:
        print("Please re-enter your password: ")
        Pword = str(input())
    #endif
    while len(Pword) < 6 or len(Pword) > 8:
        if attempt == 1:
            print("Please enter a password between 6 and 8 characters: ")
            Pword = str(input())
        #endif
        if attempt == 2:
            print("Please re-enter your password: ")
            Pword = str(input())
        #endif
    #endwhile

    #return value
    return Pword
#endprocedure


#mainprogram
first_attempt = ""
second_attempt = " "
while first_attempt != second_attempt:
    first_attempt = getPword(1)
    second_attempt = getPword(2)

    if first_attempt == second_attempt:
        print("Password change successful")
#end of program