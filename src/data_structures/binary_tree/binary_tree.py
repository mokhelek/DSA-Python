from collections import deque


class TreeNode:
    
    def __init__(self, left = None, right = None, value= 0) :
        
        self.value = value 
        self.left = left 
        self.right = right 
      
        
def pre_order(root):
    # ? root -> left -> right 
    if root:
        print(root.val, end=' ') 
        pre_order(root.left)
        pre_order(root.right)
    

def in_order(root):
    # ? left -> root -> right 
    if root:
        in_order(root.left)
        print(root.val, end=' ') 
        in_order(root.right)


def post_order(root):
    # ? left -> right -> root 
    if root:
        post_order(root.left)
        post_order(root.right)
        print(root.val, end=' ') 
        
        
def breath_first(root):
    # ? WE'LL BE USING THE QUEUE PRINCIPLE 
    
    if not root:
        return
    
    queue = deque([root])
    
    while queue:
        node = queue.popleft()
        
        print(node.value, end=' ')  # visit node
        
        if node.left:
            queue.append(node.left)
            
        if node.right:
            queue.append(node.right)
            
            
def invert_tree(root):
    
    if not root:
        return None 
    
    # ? SWAP LEFT && RIGHT CHILDREN 
    
    root.left = invert_tree(root.right) 
    root.right =  invert_tree.left(root) 
    
    return root

    
def has_path_sum(root, target):
    
    if not root:
        return False 
        
    if not root.left and not root.right:
        return target == root.val
    
    
    return has_path_sum(root.left, target - root.val) or has_path_sum(root.right, target - root.val) 


def lowest_common_ancestor(root, p, q):
    
    if root.val > p.val and root.val > q.val:
        return lowest_common_ancestor(root.left, p, q)
    
    elif root.val < p.val and root.val < q.val:
        return lowest_common_ancestor(root.right, p, q)
    
    else:
        return root
    