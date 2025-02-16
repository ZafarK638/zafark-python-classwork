x = input()
packets = [int(i) for i in x.split()]

tot = 0
packets.sort()

me = True
for i in packets:
    if me:
        tot = tot + i
        me = False
    else:
        me = True

print(tot)