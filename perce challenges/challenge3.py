inp = input()
alphabet = "abcdefghijklmnopqrstuvwxyz "
arr = set(inp)  
extra = [char for char in alphabet if char not in arr]
print("".join(extra))
