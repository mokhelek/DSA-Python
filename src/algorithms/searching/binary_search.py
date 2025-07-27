"""
Binary Search Algorithm

Given a sorted array, returns the index of the target element using binary search.

Time Complexity: O(log n)
Space Complexity: O(1)
"""


def binary_search(arr, target):
    left = 0
    right = len(arr) - 1
    
    while left <= right :
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid 
        elif arr[mid] < target:
            left = mid + 1
        else :
            right = mid - 1 
    return -1        
        

print(binary_search([1, 3, 5, 7, 9], 9))  # Output: 4
print(binary_search([1, 3, 5, 7, 9], 7))  # Output: 3
