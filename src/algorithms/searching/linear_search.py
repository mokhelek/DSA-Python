

#? SIMPLE IMPLEMENTATION 

def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i 
    return -1

numbers = [4, 2, 7, 1, 9, 3]
print(linear_search(numbers, 7))  # Output: 2
