oginput = str(input())
vowels = "aeiouAEIOU"
piglatmain = ""
for i in range(1,len(oginput)):
    piglatmain += oginput[i]

if oginput[0] not in vowels:
    piglatextra = "-" + oginput[0] + "ay"
else:
    piglatextra = "-yay"
    piglatmain = oginput[0]+piglatmain

print(piglatmain + piglatextra)