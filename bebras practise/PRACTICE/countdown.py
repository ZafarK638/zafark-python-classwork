#input start of countdown
countd = -1
while countd < 0 or countd > 100:
    countd = int(input(""))
#end while


#print numbers
while countd != 0:
  print(countd)
  countd += -1
#end while

print("lift off")