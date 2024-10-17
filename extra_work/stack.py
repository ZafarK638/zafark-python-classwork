myString = str(input ("Please enter a word or phrase to be tested: "))
list1 = list(myString) 	# --- convert myString to a list of characters 
numChars = len(list1)
Stack = list()
s = Stack()
for i in range (0,numChars-1):
	s.push(list1[i])
	# --- next i
# --- end for loop
list2 = list()
while s.isEmpty == False:
	list2.append(s.pop())
# --- end while loop
if list1 == list2:
	palindrome = True
# --- End if statement
