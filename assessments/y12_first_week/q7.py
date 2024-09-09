def find_max_in_2d_array(two_d_array):
    # Initialize the max_value to the smallest possible integer
    overall_max = float('-inf')
    max_row = -1
    max_col = -1
    
    # Iterate through each sub-array
    for row_index, sub_array in enumerate(two_d_array):
        # Iterate through each element in the current sub-array
        for col_index, num in enumerate(sub_array):
            if num > overall_max:
                overall_max = num
                max_row = row_index
                max_col = col_index
    
    # Output the highest value and its position
    print(f"The highest value is {overall_max} in row {max_row} column {max_col}.")

# Example 2D array
My_2d_array = [[0, 1, 2], [3, 5, 10], [6, 7, 8]]

# Call the function to find the max value and its position in the 2D array
find_max_in_2d_array(My_2d_array)
