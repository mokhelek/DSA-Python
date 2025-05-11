
#%%

def merge_sort(arr):
    if len(arr) > 1:
        
        mid = len(arr) // 2
        left_arr = arr[:mid]
        right_arr = arr[mid:]
        
        merge_sort(left_arr)
        merge_sort(right_arr)
        
        i = 0 # index for left_array
        j = 0 # index for right_array
        k = 0 # index for main array
        
        while i < len(left_arr) and j < len(right_arr) :
            if left_arr[i] < right_arr[j]:
                arr[k] = left_arr[i]
                i += 1
            else:
                arr[k] = right_arr[j]
                j += 1
            k += 1
            
        while i < len(left_arr):
            arr[k] = left_arr[i]
            i += 1
            k += 1
            
        while j < len(right_arr):
            arr[k] = right_arr[j]
            j += 1
            k += 1




arr = [12, 11, 13, 5, 6, 7]
merge_sort(arr)
print("Sorted array:\n", arr)
# %%
