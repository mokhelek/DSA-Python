"""
 * Question: Given a sorted array with duplicates, find the first occurrence of a target value.

"""

def first_occurrence(arr, target):
    min = 0
    max = len(arr) - 1
    result = -1
    
    while min <= max:
        mid = (min + max) // 2
        if arr[mid] == target:
            result = mid
            max = mid -1  # ? Keep looking left
        elif arr[mid] < target:
            min = mid + 1
        else:
            max = mid -1
    return result    


print(first_occurrence([1, 2, 2, 2, 3, 4], 2))  # Output: 1
print(first_occurrence([1, 2, 2, 2, 3, 4], 5))  # Output: -1
