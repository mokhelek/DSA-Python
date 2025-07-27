
"""
Remove Duplicates from Sorted Array

Removes duplicates from a sorted array in-place and returns the number of unique elements.

Time Complexity: O(n)
Space Complexity: O(1)
"""

def remove_duplicates(sorted_array):

    # If the array is empty or has only one element, return 0 (or 1 if you want to count single elements)
    if len(sorted_array) <= 1:
        return len(sorted_array)

    # Pointer that keeps track of the index where the next unique element should be placed
    unique_index = 0

    # Loop through the array from start to end
    for current_index in range(len(sorted_array)):
        # If the current element is not the same as the previous one, it's unique
        if sorted_array[current_index] != sorted_array[current_index - 1]:
            # Place the unique element at the position pointed to by unique_index
            sorted_array[unique_index] = sorted_array[current_index]
            unique_index += 1

    # Return the number of unique elements
    return unique_index
