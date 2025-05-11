
''' 
    #? Question: Suppose an array sorted in ascending order is 
    #? rotated at some pivot. Find the minimum element (modified binary search).
'''
#  if mid is less than max index value
#  then, minimum would have to be on the right side of the array
#  Therefore we can perform binary search on the right side
#  EDGE CASE : IF FIRS ELEMENT IS SMALLER THAN LAST ELEMENT (ARR IS ALREADY SORTED)
# 

#%%

def find_min_rotated(arr):
    min = 0 
    max = len(arr) - 1
    
    if arr[min] < arr[max]:
        return min
        
    while min < max:
        mid = (min + max) // 2
        if arr[mid] > arr[max]:
            min = mid + 1
        else:
            max = mid -1
    return arr[min]
            
    
# Test cases
print(find_min_rotated([4, 5, 6, 7, 0, 1, 2]))  # Output: 0
print(find_min_rotated([3, 4, 5, 1, 2]))       # Output: 1


# %%
# ? Question: Search for a target value in a rotated sorted array (no duplicates).

# FIND THE ROTATION POINT
# DIVIDE THE ARRAY IN 2 (THE ROTATION POINT)
# PERFORM BINARY SEARCH ON BOTH


def findPivot(nums):
    left, right = 0, len(nums) - 1

    while left < right:
        mid = (left + right) // 2
        if nums[mid] > nums[right]:
            left = mid + 1
        else:
            right = mid
    return left

def binarySearch(nums, left, right, target):
    while left <= right:
        mid = (left + right) // 2
        if nums[mid] == target:
            return mid 
        elif nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1 
    return -1 


def search_rotated(nums, target):
    
    if not nums:
        return -1

    pivotPoint = findPivot(nums)

    # If the array is not rotated, do a normal binary search
    if pivotPoint == 0:
        return binarySearch(nums, 0, len(nums) - 1, target)

    # Determine which half to search
    if nums[0] <= target <= nums[pivotPoint - 1]:
        return binarySearch(nums, 0, pivotPoint - 1, target)
    else:
        return binarySearch(nums, pivotPoint, len(nums) - 1, target)

    

# Test cases
print(search_rotated([3, 1], 3))  # Output: 4
print(search_rotated([4, 5, 6, 7, 0, 1, 2], 2))  # Output: 6


# %%
