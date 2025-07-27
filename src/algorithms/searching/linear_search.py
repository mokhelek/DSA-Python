"""
Linear Search Algorithm

Given an array, returns the index of the target element using linear search.

Time Complexity: O(n)
Space Complexity: O(1)
"""

def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i 
    return -1

numbers = [4, 2, 7, 1, 9, 3]
print(linear_search(numbers, 7))  # Output: 2
