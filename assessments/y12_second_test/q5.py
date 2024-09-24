def diagonal_difference(matrix):
    n = len(matrix)  # Get the number of rows (assuming a square matrix)
    primary_diagonal_sum = 0
    secondary_diagonal_sum = 0
    
    for i in range(n):
        primary_diagonal_sum += matrix[i][i]  # Sum of primary diagonal
        secondary_diagonal_sum += matrix[i][n-1-i]  # Sum of secondary diagonal
    
    difference = abs(primary_diagonal_sum - secondary_diagonal_sum)  # Absolute difference
    return primary_diagonal_sum, secondary_diagonal_sum, difference

# Test the function
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

primary_sum, secondary_sum, difference = diagonal_difference(matrix)
print(f"Primary Diagonal Sum: {primary_sum}")  # Output: 15
print(f"Secondary Diagonal Sum: {secondary_sum}")  # Output: 15
print(f"Difference: {difference}")  # Output: 0
