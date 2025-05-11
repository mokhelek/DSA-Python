

#%%

# Problem: Given a sorted array nums, remove the duplicates in-place such that each element appears 
# only once and return the new length.

def remove_duplicates(arr):
    if len(arr) <=1:
        return 0
    
    write = 0
    
    for i in range(len(arr)):
        if arr[i] != arr[i - 1]:
            arr[write] = arr[i]
            write += 1
    return write


print(remove_duplicates([1,2,2,4,4,5,7]))
# %%
