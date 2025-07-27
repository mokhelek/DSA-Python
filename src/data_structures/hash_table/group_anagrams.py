"""
Group Anagrams Using Hash Table

Groups a list of strings into anagrams.

Time Complexity: O(n * k log k) where n is the number of strings and k is the maximum string length.
Space Complexity: O(n)
"""

#%%v
def group_anagrams(arr):
    groups = {}
     
    for s in arr:
         key = ''.join(sorted(s))
         if key not in groups:
             groups[key] = []
         groups[key].append(s)
    return list(groups.values())

print(group_anagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))
# %%
