# Initialize variables
numbers = []
total = 0

while True:
    # Prompt the user for a number
    num = int(input("Enter a positive integer (negative to stop): "))
    
    # Check if the number is negative
    if num < 0:
        break
    
    # Add the number to the list
    numbers.append(num)

# Calculate and print the average if numbers were entered
if numbers:
    average = sum(numbers) / len(numbers)
    print(f"The average of the entered numbers is: {average:.2f}")
else:
    print("No positive numbers were entered.")
