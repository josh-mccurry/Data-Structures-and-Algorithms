import random

# Sorting Algorithms

rand_list = list(range(1, 5000))
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

print(f"Sorted List: {insertion_sort(rand_list)}")