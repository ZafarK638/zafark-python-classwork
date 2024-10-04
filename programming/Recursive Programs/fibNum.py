import time

# Recursive Fibonacci function
def fib(n: int):
    if n <= 1:
        return n
    else: 
        return fib(n-1) + fib(n-2)
    # end if statement
# end procedure

# Iterative Fibonacci function using list
def fibonacci2(n):
    fibNumbers = [0, 1]  # List of the first two Fibonacci numbers
    # Append the sum of the two previous numbers to the list
    for i in range(2, n+1):  # Loop from 2 to n (inclusive)
        fibNumbers.append(fibNumbers[i-1] + fibNumbers[i-2])
    return fibNumbers[n]  # Return the nth Fibonacci number

# Function to print Fibonacci sequence for recursive method
def print_fib_sequence_recursive(n):
    print("Recursive Fibonacci sequence for n =", n)
    for i in range(n):
        print(fib(i), end=" ")
    print("\n")

# Function to print Fibonacci sequence for iterative method
def print_fib_sequence_iterative(n):
    print("Iterative Fibonacci sequence for n =", n)
    fibNumbers = [fibonacci2(i) for i in range(n)]
    print(" ".join(map(str, fibNumbers)))
    print("\n")

# Function to measure and print the time taken for each method
def measure_time():
    # User input for n
    while True:
        n = int(input("Enter the value of n (between 3 and 30): "))
        if 3 <= n <= 30:
            break
        else:
            print("Please enter a valid number between 3 and 30.")

    # Timing the recursive Fibonacci
    print("Timing recursive Fibonacci...")
    startTime1 = time.time()
    print_fib_sequence_recursive(n)
    endTime1 = time.time()
    print(f"Time taken for recursive Fibonacci: {endTime1 - startTime1} seconds\n")

    # Timing the iterative Fibonacci
    print("Timing iterative Fibonacci...")
    startTime2 = time.time()
    print_fib_sequence_iterative(n)
    endTime2 = time.time()
    print(f"Time taken for iterative Fibonacci: {endTime2 - startTime2} seconds\n")

# Function to measure time for n = 10 and n = 20
def time_for_n10_n20():
    print("\n--- Timing for n = 10 ---")
    print("Recursive:")
    startTime1 = time.time()
    print_fib_sequence_recursive(10)
    endTime1 = time.time()
    print(f"Time taken: {endTime1 - startTime1} seconds\n")

    print("Iterative:")
    startTime2 = time.time()
    print_fib_sequence_iterative(10)
    endTime2 = time.time()
    print(f"Time taken: {endTime2 - startTime2} seconds\n")

    print("\n--- Timing for n = 20 ---")
    print("Recursive:")
    startTime1 = time.time()
    print_fib_sequence_recursive(20)
    endTime1 = time.time()
    print(f"Time taken: {endTime1 - startTime1} seconds\n")

    print("Iterative:")
    startTime2 = time.time()
    print_fib_sequence_iterative(20)
    endTime2 = time.time()
    print(f"Time taken: {endTime2 - startTime2} seconds\n")

# Main Program
def main():
    measure_time()  # Allow user to enter n between 3 and 30
    time_for_n10_n20()  # Measure time for n = 10 and n = 20

if __name__ == "__main__":
    main()
