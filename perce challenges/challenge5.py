inp = input()
pi_digits = "31415926535897932384626433832795028841971693993751"
inp = inp.replace(" ", "")
encrypted = []
    
for i, char in enumerate(inp):
    shift = int(pi_digits[i]) 
    if i % 2 == 0: 
        new_char = chr(((ord(char) - ord('A') + shift) % 26) + ord('A'))
    else:  
        new_char = chr(((ord(char) - ord('A') - shift) % 26) + ord('A'))
    encrypted.append(new_char)
    
print("".join(encrypted))
