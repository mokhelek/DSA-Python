
#%%
#? A peak element is an element that is greater than its neighbors. Given an input array 
#? nums, find a peak element (there may be multiple peaks, return any one).

def find_peak_element(arr):
    
    left = 0
    right = len(arr) -1 
    
    while left < right:
        mid = (left + right) // 2
        if arr[mid] > arr[mid + 1]:
            # descending slope
            right = mid
        else:
            # ascending slope
            left = mid + 1
    return left            
            
    
# Test cases
print(find_peak_element([1, 2, 3, 1]))         # Output: 2
print(find_peak_element([1, 2, 1, 3, 5, 6, 4])) # Output: 5 (or 1)
# %%
