def sum_of_even_numbers(n: int):
    count = 2
    total = 0
    while count <= n:
        total += count
        count += 2  
    #endwhile
    return total
#endprocedure

# Call the function
print(sum_of_even_numbers(10))
