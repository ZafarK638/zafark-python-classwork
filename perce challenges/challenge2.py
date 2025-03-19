num = input()
temp = int(num)
count = 1
while temp > 0:
    arr = [int(d) for d in str(temp)]
    temp2 = 0
    for i in range(len(arr)):
        temp2 += arr[i]
    #next i
    temp += -temp2
    count += 1
print(count)