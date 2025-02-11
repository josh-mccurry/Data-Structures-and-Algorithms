import random

# Sorting Algorithms

# Generate a randomized list of values that span the range
rand_list = list(range(1, 200))
random.shuffle(rand_list)

# BUBBLE SORT
# Best Case: O(n)
# Average Case: O(n^2)
# Worst Case: O(n^2)

def bubble_sort(list):

    print(f"Unsorted Array: {rand_list}")

    for i in range(len(list) - 1):
        for j in range(len(list) - i - 1):
            if list[j] > list[j + 1]:
                list[j], list[j+1] = list[j + 1], list[j]    

    return list   

#print(f"Sorted List:  {bubble_sort(rand_list)}")

# SELECTION SORT
# Best Case: O(n^2)
# Average Case: O(n^2)
# Worst Case: O(n^2)

def selection_sort(list):

    print(f"Unsorted List: {rand_list}")

    for i in range(len(list) - 1):
        min_index = i
        for j in range(i + 1, len(list)):
            if list[j] < list[min_index]:
                min_index = j
        if min_index != i:
            list[i], list[min_index] = list[min_index], list[i]
    
    return list

#print(f"Sorted List {selection_sort(rand_list)}")

# INSERTION SORT
# Best Case: O(n)
# Average Case: O(n^2)
# Worst Case: O(n^2)

def insertion_sort(list):

    print(f"Unsorted List: {rand_list}")

    for i in range(1, len(list)):
        key = list[i]
        j = i - 1
        while (j >= 0 and list[j] > key):
            list[j + 1] = list[j]
            j = j - 1
        list[j + 1] = key
    
    return list

#print(f"Sorted List: {insertion_sort(rand_list)}")

# MERGE SORT
# Best Case: O(n log n)
# Average Case: O(n log n)
# Worst Case: O(n log n)

def merge_sort(list):

    if len(list) <= 1:
        return list
    
    # Locate the middle and divide the list into two halves
    mid = len(list) // 2
    left_half = list[:mid]
    right_half = list[mid:]

    # recursively invoke merge_sort on the halves
    left_half = merge_sort(left_half)
    right_half = merge_sort(right_half)

    # pass the halves to merge
    return merge(left_half, right_half)

def merge(left, right):
    
    # establish the left most values in each half
    result = []
    left_index, right_index = 0, 0

    # Loop through both halves
    while left_index < len(left) and right_index < len(right):
        # Determine which half is less than the other and append it to result
        if left[left_index] <= right[right_index]:
            result.append(left[left_index])
            left_index += 1
        else:
            result.append(right[right_index])
            right_index += 1
    
    # Appends any remaining elements from left list (in the event right list was emptied first)
    result.extend(left[left_index:])
    # Appends any remaining elements from right list (in the event left list was emptied first)
    result.extend(right[right_index:])

    return result

#print(f"Unsorted List: {rand_list}")
#print(f"Sorted List: {merge_sort(rand_list)}")

# QUICK SORT
# Best Case: O(n log n)
# Average Case: O(n log n)
# Worst Case: O(n^2)

def quick_sort(list, start_index, end_index):

    if start_index >= end_index:
        return
    
    p = partition(list, start_index, end_index)

    quick_sort(list, start_index, p - 1)
    quick_sort(list, p + 1, end_index)

def partition(list, start_index, end_index):
    
    pivot = list[start_index]
    low = start_index + 1
    high = end_index

    while True:
        while low <= high and list[high] >= pivot:
            high = high - 1
        
        while low <= high and list[low] <= pivot:
            low = low + 1
        
        if low <= high:
            list[low], list[high] = list[high], list[low]
        else:
            break

    list[start_index], list[high] = list[high], list[start_index]
    
    return high

print(f"Unsorted List: {rand_list}")
quick_sort(rand_list, 0, len(rand_list) - 1)
print(f"Sorted List: {rand_list}")
