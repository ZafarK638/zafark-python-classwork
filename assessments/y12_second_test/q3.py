def sum_rows(matrix):
    final_matrix = []  # Initialize an empty list to store the row sums
    for i in range(len(matrix)):  # Loop through rows
        total = 0  # Reset total for each row
        for j in range(len(matrix[i])):  # Loop through columns
            total += matrix[i][j]
        final_matrix.append(total)  # Add the row sum to final_matrix
    return final_matrix

# Test the function
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
print(sum_rows(matrix))  # Output: [6, 15, 24]
