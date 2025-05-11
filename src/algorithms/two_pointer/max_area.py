
#%%

def max_area(height):
    left = 0
    right = len(height) -1
    maxArea = 0
    
    while left < right:
        h = min(height[left], height[right])
        w = right - left 
        area =  h * w 
        maxArea = max(maxArea, area)
        
        if height[left] < height[right]:
            left += 1
        else:
            right -=1 
    return maxArea
    

height = [1,8,6,2,5,4,8,3,7]
max_area(height)

# %%
