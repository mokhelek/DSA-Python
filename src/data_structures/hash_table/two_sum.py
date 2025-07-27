
#%%

#? Given a list of numbers and a target, return the 2 indexes that sum up to the target

def two_sum(arr, target):
    
    seen = {}  # Hashmap for keeping track of what we've seen
    
    for i, num in enumerate(arr):
        compliment  = target - num # the value we need to sum with num to get the target
        if compliment in seen:
            return [ seen[compliment] , i ]
        seen[num] = i 
    return [] 


arr = [2, 5, 7, 7 ,2 ,3]

print( two_sum(arr, 14))
# %%
