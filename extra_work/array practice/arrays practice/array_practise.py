numbers = []
total = 0
#definingvariables

for i in range(0,6):
	add_to_array = int(input("Enter a number (You will have to enter 6 in total): "))
	numbers.append(add_to_array)
#endofloop


for i in range(0,6):
	j = i + (-6)
	print(numbers[j])
	total = total + int(numbers[j])
#endofloop
mean = total/6
print(total)
print(mean)
