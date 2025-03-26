exList = list(input().split(" "))
size = len(exList)
streak = 1
streak_record = streak
for i in range(1,size):
    if exList[i] < exList[i-1]:
        streak = 0
    else: 
        streak += 1
    if streak > streak_record:
        streak_record = streak
print(streak_record)
