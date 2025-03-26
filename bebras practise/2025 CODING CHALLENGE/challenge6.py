num_list = list(input().split(" "))
first = int(num_list[0])
last = int(num_list[1])
final = 0
if first%2 == 1:
    first += 1
if last%2 == 1:
    last += -1
range = int((last-first)/2)
for i in range(range):
    final += first + (i*2)  
print(final)