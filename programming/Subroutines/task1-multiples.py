def multiples(table,startnum,endnum,pupilname)->None:
    print("Hi, ",pupilname,"... here is your times table: ")
    count = startnum
    while count < (endnum+1):
        cor_ans = table*count
        print(table,"x",count,"=","?")
        use_ans = ""
        while use_ans != cor_ans:
            use_ans = int(input())
            if use_ans == cor_ans:
                print("Correct!")
            else:
                print("Incorrect!") 
            #endif
        #endwhile
        count += 1
#endprocedure


print("What is your name? ")
pupilname = str(input())
print("Enter times table, start number and end number: ")
table = int(input())
startnum = int(input())
endnum = int(input())
multiples(table,startnum,endnum,pupilname)