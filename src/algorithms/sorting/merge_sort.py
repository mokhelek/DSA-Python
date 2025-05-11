"""
PROBLEM: Given an unsorted array of int values, sort the array(in-place)


SPACE-TIME COMPLEXITY
> O(n log n) Time
> O(n) space 


APPROACH:
> Divide:  Divide the array recursively into two halves until it can no more be divided. 
> Conquer:  Each sub-array is sorted individually using the merge sort algorithm. 
> Merge:  The sorted sub-arrays are merged back together in sorted order. 
          The process continues until all elements are merged. 

"""

def merge_sort(arr):
    
    if len(arr) > 1:
        
        # DIVIDING THE ARRAY IN 2
        mid = len(arr) // 2
        left_arr = arr[:mid]
        right_arr = arr[mid:]
        
        # RECURSIVELY APPLY THE MERGE-SORT WHILE ARR IS > 1
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
            
        # NOW, COPY THE REMAINING ELEMENTS OF THE left_arr[] or right_arr[] (if any)
            
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


