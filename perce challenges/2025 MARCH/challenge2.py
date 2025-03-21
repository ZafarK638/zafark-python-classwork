inp, n = int(input()), int(input())
for i in range(1,n):
    inp *= 5
    while inp%10 == 0:
        inp = int(inp/10)
    #next while
#next i
print(inp)