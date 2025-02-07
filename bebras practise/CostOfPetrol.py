petrol = input().split()
while len(petrol) != 12:
    petrol = input().split()
for i in range (len(petrol)):
    if int(petrol[i]) > 200 or int(petrol[i]) < 0 or int(petrol[i]) % 1 != 0:
        petrol = input().split()
tot_petrol = float(0.0)
for i in range(len(petrol)):
    tot_petrol += (float(petrol[i])*0.0024)

print(int(tot_petrol))