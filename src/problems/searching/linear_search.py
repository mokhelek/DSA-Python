

#? Question: Modify linear search to return all indices where the target appears in the array.

def linear_search_all(arr, target):
    result = []
    for i in range(len(arr)):
        if arr[i] == target:
            result.append(i)
    return result if result else -1

print(linear_search_all([4, 2, 7, 2, 9], 2))  # Output: [1, 3]
print(linear_search_all([4, 2, 7, 2, 9], 5))  # Output: -1
#%%

#? Question: Find the last occurrence of a target value in an array using linear search.

def last_occurrence(arr, target):
    for i in range(len(arr)-1, 0, -1):
        if arr[i] == target:
            return i
    return -1  

# Test cases
print(last_occurrence([4, 2, 7, 2, 9], 2))  # Output: 3
print(last_occurrence([4, 2, 7, 2, 9], 5))  # Output: -1

# %%
