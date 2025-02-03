from math import *

arr_unsorted = [8, 2, 32, 128, 1, 512, 4, 1024, 2048, 256, 64, 16]
arr = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048]
inter_arr = list(range(1, 100))


# Searching Algorithms

# LINEAR SEARCH
# Best Case: O(1)
# Average Case: O(n)
# Worst Case: O(n)
# Works both sorted and unsorted

def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            print("Target value {} found at index {}".format(target, i))
            return i
        print("{} at index {} is not the target value {}".format(arr[i], i, target))
    return -1

#linear_search(arr, 256)

# BINARY SEARCH
# Best Case: O(1)
# Average Case: O(log n)
# Worst Case: O(log n)
# Must be sorted

def binary_search(arr, target):
    low = 0
    high = len(arr) - 1
    mid = 0
 
    while low <= high:
        mid = (high + low) // 2
 
        if arr[mid] < target:
            print("{} at index {} is not the target value {}".format(arr[mid], mid, target))
            low = mid + 1
 
        elif arr[mid] > target:
            print("{} at index {} is not the target value {}".format(arr[mid], mid, target))
            high = mid - 1
 
        else:
            print("Target value {} found at index {}".format(target, mid))
            return mid
 
    # If we reach here, the element was not present
    return -1

#binary_search(arr, 2048)

# INTERPOLATION SEARCH
# Best Case: O(1)
# Average Case: O(log(log n))
# Worst Case: O(n)
# Performance improves with a sequence of consecutive integers
# Performance degrades with a sequence of exponential integers

def interpolation_search(arr, target):
    start = 0
    end = len(arr) - 1
    found = False

    while start <= end and target >= arr[start] and target <= arr[end]:
        probe = start + (target - arr[start]) * (end - start) // (arr[end] - arr[start])

        print("Position is {}".format(probe))

        if arr[probe] == target:
            print("Target value {} found at index {}".format(target, arr[probe]))
            return probe

        if arr[probe] < target:
            print("{} at index {} is not the target value {}".format(arr[probe], probe, target))
            start = probe + 1
        
        else:
            print("{} at index {} is not the target value {}".format(arr[probe], probe, target))
            end = probe - 1

    return -1

interpolation_search(inter_arr, 76)