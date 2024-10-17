myString = str(input ("Please enter a word or phrase to be tested: "))
list1 = list(myString) 	# --- convert myString to a list of characters 
numChars = len(list1)
s = list()
palindrome = False
for i in range (numChars):
	s.append(list1[i])
	# --- next i
# --- end for loop
list2 = list()
while len(s) == 0:
	list2.append(s.pop())
# --- end while loop
if list1 == list2:
	palindrome = True
# --- End if statement
if palindrome:
	print("This is a palindrome. ")
else:
	print("This is not a palindrome. ")