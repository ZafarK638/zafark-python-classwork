x = input()
chocolates = [int(i) for i in x.split()]
tot = 0
chocolates.sort()
me = True
for i in chocolates:
    if me:
        tot = tot + i
        me = False
    else:
        me = True
print(tot)