def bubble_sort(list):
    n = len(list)
    for i in range(n - 1):
        for j in range(n - i - 1):
            if list[j] > list[j + 1]:
                list[j], list[j + 1] = list[j + 1], list[j]
            #end if statement
        #end j for loop
    #end i for loop
    return list
#end procedure


array = []

print("How long do you want the list to be?")
len_of_list = int(input())
print("Please enter the values in the list")
for i in range(len_of_list):
    array.append(int(input()))
#next i

print("Unsorted array:", array)
sorted_array = bubble_sort(array)
print("Sorted array:", sorted_array)