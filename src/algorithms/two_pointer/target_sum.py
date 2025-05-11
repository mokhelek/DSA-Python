#%%
#? Problem: Given a sorted array of integers and a target sum, 
#? return the indices of the two numbers that add up to the target.


def two_sum_sorted(arr, target):
    left = 0
    right = len(arr) -1
    
    while left < right:
        sum = arr[left] + arr[right]
        if sum == target:
            return [left, right]
        elif sum < target:
            left += 1
        else:
            right -=1
    return []


arr = [1, 2, 3, 4, 6]
target = 5

two_sum_sorted(arr, target)
# %%
