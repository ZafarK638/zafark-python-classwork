import time
import random

# Bubble Sort
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

# Insertion Sort
def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

# Compare sorting times
def compare_sorting_times(n):
    # Generate a random list of n numbers
    random_list = [random.randint(0, 10000) for _ in range(n)]

    # Time Bubble Sort
    bubble_list = random_list.copy()
    start_time = time.time()
    bubble_sort(bubble_list)
    bubble_sort_time = time.time() - start_time

    # Time Insertion Sort
    insertion_list = random_list.copy()
    start_time = time.time()
    insertion_sort(insertion_list)
    insertion_sort_time = time.time() - start_time

    return bubble_sort_time, insertion_sort_time

# Test the algorithm with a sample value of n
n = 10000  # Experiment with different values of n
bubble_time, insertion_time = compare_sorting_times(n)
bubble_time, insertion_time
