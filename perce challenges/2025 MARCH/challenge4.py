n = int(input())
arr = []
final_answer = []
for i in range(n-1):
    arr.append(int(input()))

for i in range(len(arr)):
    arr2 = []
    for k in range(1,n):
        arr2.append(k)
        
    for j in range(0,n-1):
        num = list(str(arr[j]))
        for k in range(len(arr2)):
            if int(num[i]) == arr2[k-1]:
                arr2.pop()
        print(arr2)
