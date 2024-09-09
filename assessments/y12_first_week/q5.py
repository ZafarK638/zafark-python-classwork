def find_max_value(arr):
    # Check if the array is not empty
    if not arr:
        print("The array is empty.")
        return
    
    # Initialize the max_value with the first element
    max_value = arr[0]
    
    # Iterate through the array to find the maximum value
    for num in arr:
        if num > max_value:
            max_value = num
    
    # Output the highest value
    return max_value

# Example array
my_array = [8, 1, -6, 9, 15, 7, 2]

# Call the function
find_max_value(my_array)
