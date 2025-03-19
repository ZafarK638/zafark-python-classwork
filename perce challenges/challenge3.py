inp = input()
alphabet = "abcdefghijklmnopqrstuvwxyz "
arr = set(inp)  # Use a set for fast lookup
extra = [char for char in alphabet if char not in arr]
print("".join(extra))
