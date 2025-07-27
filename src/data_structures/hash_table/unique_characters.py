

#%% 
def first_uniq_char(string):
    
    freq = {} 
    
    for char in string:
        freq[char] = freq.get(char, 0) + 1
        
    for i, char in enumerate(string):
        if freq[char] == 1:
            return i 
    return -1 


print(first_uniq_char("madam") )
# %%
