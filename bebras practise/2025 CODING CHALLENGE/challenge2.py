num_list = list(input().split(", "))
size = len(num_list)
total = 0
for i in range(size):
    current_sum = 0
    for j in range(i,size):
        current_sum = current_sum + int(num_list[j])
        total = max(total, current_sum)
    #next j
#next i
print(total)


#not sure why this doesn't work
