# Initialize an empty list to store the integers
numbers = []

# Loop to get 10 positive integers from the user
for i in range(10):
    while True:
        try:
            num = int(input(f"Enter positive integer {i+1}: "))
            if num > 0:
                numbers.append(num)
                break
            else:
                print("Please enter a positive integer.")
        except ValueError:
            print("That's not a valid integer. Try again.")

# Calculate the total
total = sum(numbers)

# Output the total with a meaningful message
print(f"\nThe sum of the ten positive integers is: {total}")
