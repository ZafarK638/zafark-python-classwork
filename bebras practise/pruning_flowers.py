# get input
f = input().split()
pickedF = []

for i in f:
    if i not in pickedF:
        pickedF.append(i)

printword = ""
for i in range(len(pickedF)):
   printword += pickedF[i] + " "

print(printword)
