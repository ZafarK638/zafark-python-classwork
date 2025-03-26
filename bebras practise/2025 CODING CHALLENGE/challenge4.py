wordList = list(input().split(" "))
size = len(wordList)
count = 0
for i in range(size):
    for j in range(i+1,size):
        if wordList[i] == wordList[j]:
            count += 1
        #end if statement
    #next j
#next i
if count > 0:
    print("Not unique")
else: 
    print("Unique")