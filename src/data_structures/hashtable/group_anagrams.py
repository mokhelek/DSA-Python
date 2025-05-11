
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
