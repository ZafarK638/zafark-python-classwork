pay = list(map(int, input().split()))
total = 0
days = 0

for i in pay:
    total += i
    total += -20
    days += 1
    if total >= 1000:
        break

print(days)