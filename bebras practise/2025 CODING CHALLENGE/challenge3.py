performer_list = input()
size = len(performer_list)
count = 1
perf = 0
temp = performer_list[0]
for i in range(1,size):
    if str(performer_list[i]) == str(temp):
        count += 1
    else:
        count = 1
    if count > perf:
        perf = count
    temp = performer_list[i]
#next i
if perf == 1:
    perf = 0
print(perf)