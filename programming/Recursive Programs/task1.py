def sum_even(n):
    # Base case: if n is 0, return 0
    if n == 0:
        return 0
    else:
        # Recursive case: return n + sum_even(n - 2)
        return n + sum_even(n - 2)

# Main program to call the recursive routine
n = int(input("Enter an even number: "))

# Ensure the input is an even number
if n % 2 == 0:
    # Call the sum_even function and store the result
    result = sum_even(n)
    
    # Output the result
    print(f"The sum of all even numbers between 0 and {n} is: {result}")
else:
    print("Please enter a valid even number.")
