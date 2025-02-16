months = list(map(int, input().split()))
fuel = sum(months)
co_two = 0.0024 * fuel
print(int(co_two))