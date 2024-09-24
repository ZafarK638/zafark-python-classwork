def largest_in_rows(matrix):
    final_matrix = []  # Initialize an empty list to store the largest number from each row
    for i in range(len(matrix)):  # Loop through rows
        largest = max(matrix[i])  # Find the largest number in the current row
        final_matrix.append(largest)  # Add the largest number to final_matrix
    return final_matrix

# Test the function
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
print(largest_in_rows(matrix))  # Output: [3, 6, 9]
