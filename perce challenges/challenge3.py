inp = str(input())
arr = [str(d) for d in str(inp)]
alph = "abcdefghijklmnopqrstuvwxyz "
alphabet = [str(x) for x in str(alph)]
extra = alphabet
for i in range(len(arr)):
    count = 0
    for j in range(len(alphabet)):
        if arr[i] != alphabet[j]:
            pass
        else:
            count += 1
        if count == 0 and j == 26:
            extra[j] = ""
    #next j
#next i
extra[j] = "1"
print(extra)