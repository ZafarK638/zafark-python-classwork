n = int(input())
count = 0

def num_repeats(l):
    list = []
    for i in l:
        if i not in list:
            list.append(i)
    return len(l) - len(list)

for i in range(n):
    scores = [int(s) for s in input().split()]
    sort = sorted(scores)

    if sort == scores and num_repeats(scores) == 0:
        count += 1

print(count)