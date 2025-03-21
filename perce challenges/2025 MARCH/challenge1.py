inp1, inp2, inp3 = int(input()), int(input()), int(input())
inp1 *= 1.1
inp2 *= 1.1
inp3 *= 1.1
inp1 -= inp1%1
inp2 -= inp2%1
inp3 -= inp3%1
final_cost = inp1+inp2+inp3
print(int(final_cost))