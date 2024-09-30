
# Initialize an array with 6 numbers
numbers = [0, 1, 2, 3, 4, 5]

# Initialize total to 0
total = 0

# Output numbers in reverse order and calculate the total
for i in range(6):
    j = 5 - i  # Get the reverse index
    print(numbers[j])
    total += numbers[j]

# Calculate the mean
mean = total / 6

# Output the total and the mean
print("Total:", total)
print("Mean:", mean)
