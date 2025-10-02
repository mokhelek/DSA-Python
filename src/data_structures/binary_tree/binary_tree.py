"""
Binary Tree Utilities

This module provides implementations for:
- Binary tree traversals (pre-order, in-order, post-order, breadth-first/level order).
- Invert (mirror) tree.
- Path sum problem.
- Lowest common ancestor (LCA).
- Height, depth, diameter, node counting.
- Check if tree is balanced.
- Serialize & deserialize (LeetCode-style).
- Check symmetry.

Useful for studying Binary Trees and preparing for coding interviews.
"""

from collections import deque


class TreeNode:
    """
    A basic binary tree node class.
    Each node has:
    - value: data stored in the node
    - left: reference to left child
    - right: reference to right child
    """
    def __init__(self, value=0, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


# -------------------------
# TRAVERSALS
# -------------------------

def pre_order(root):
    """
    Pre-order Traversal (DFS):
    Visit root -> left -> right
    """
    if root:
        print(root.value, end=" ")
        pre_order(root.left)
        pre_order(root.right)


def in_order(root):
    """
    In-order Traversal (DFS):
    Visit left -> root -> right
    (For BSTs, this gives sorted order!)
    """
    if root:
        in_order(root.left)
        print(root.value, end=" ")
        in_order(root.right)


def post_order(root):
    """
    Post-order Traversal (DFS):
    Visit left -> right -> root
    """
    if root:
        post_order(root.left)
        post_order(root.right)
        print(root.value, end=" ")


def breadth_first(root):
    """
    Breadth-first Traversal (Level Order).
    Uses a queue (FIFO).
    """
    if not root:
        return
    queue = deque([root])
    while queue:
        node = queue.popleft()
        print(node.value, end=" ")
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)


# -------------------------
# INVERT TREE
# -------------------------

def invert_tree(root):
    """
    Invert / Mirror a binary tree.
    Swap left and right children recursively.
    """
    if not root:
        return None
    root.left, root.right = invert_tree(root.right), invert_tree(root.left)
    return root


# -------------------------
# PATH SUM
# -------------------------

def has_path_sum(root, target):
    """
    Check if there exists a root-to-leaf path where
    the sum of node values equals 'target'.
    """
    if not root:
        return False

    # Leaf node check
    if not root.left and not root.right:
        return target == root.value

    return (has_path_sum(root.left, target - root.value) or
            has_path_sum(root.right, target - root.value))


# -------------------------
# LOWEST COMMON ANCESTOR (LCA)
# -------------------------

def lowest_common_ancestor(root, p, q):
    """
    Find the Lowest Common Ancestor of two nodes in a BST.
    Assumes p and q exist in the tree.
    """
    if not root:
        return None

    if root.value > p.value and root.value > q.value:
        return lowest_common_ancestor(root.left, p, q)

    elif root.value < p.value and root.value < q.value:
        return lowest_common_ancestor(root.right, p, q)

    else:
        return root


# -------------------------
# HEIGHT / DEPTH / COUNT
# -------------------------

def max_depth(root):
    """Return the maximum depth (height) of the binary tree."""
    if not root:
        return 0
    return 1 + max(max_depth(root.left), max_depth(root.right))


def min_depth(root):
    """Return the minimum depth from root to a leaf."""
    if not root:
        return 0
    if not root.left:
        return 1 + min_depth(root.right)
    if not root.right:
        return 1 + min_depth(root.left)
    return 1 + min(min_depth(root.left), min_depth(root.right))


def count_nodes(root):
    """Return the total number of nodes in the tree."""
    if not root:
        return 0
    return 1 + count_nodes(root.left) + count_nodes(root.right)


# -------------------------
# CHECK BALANCED
# -------------------------

def is_balanced(root):
    """
    Check if the tree is height-balanced.
    A tree is balanced if:
      abs(height(left) - height(right)) <= 1
    for all nodes.
    """

    def check(node):
        if not node:
            return 0
        left = check(node.left)
        if left == -1:  # Not balanced
            return -1
        right = check(node.right)
        if right == -1 or abs(left - right) > 1:
            return -1
        return 1 + max(left, right)

    return check(root) != -1


# -------------------------
# DIAMETER OF TREE
# -------------------------

def diameter(root):
    """
    Diameter = longest path between any 2 nodes.
    Path may or may not pass through the root.
    """

    diameter_val = [0]

    def dfs(node):
        if not node:
            return 0
        left = dfs(node.left)
        right = dfs(node.right)
        diameter_val[0] = max(diameter_val[0], left + right)
        return 1 + max(left, right)

    dfs(root)
    return diameter_val[0]


# -------------------------
# SYMMETRY
# -------------------------

def is_symmetric(root):
    """
    Check if the tree is symmetric (mirror of itself).
    """

    def is_mirror(t1, t2):
        if not t1 and not t2:
            return True
        if not t1 or not t2:
            return False
        return (t1.value == t2.value and
                is_mirror(t1.left, t2.right) and
                is_mirror(t1.right, t2.left))

    return is_mirror(root, root)


# -------------------------
# SERIALIZE & DESERIALIZE
# -------------------------

def serialize(root):
    """
    Serialize a tree to a string (level order).
    Example: "1,2,3,null,null,4,5"
    """
    if not root:
        return ""
    result = []
    queue = deque([root])
    while queue:
        node = queue.popleft()
        if node:
            result.append(str(node.value))
            queue.append(node.left)
            queue.append(node.right)
        else:
            result.append("null")
    # Remove trailing nulls for cleaner output
    while result and result[-1] == "null":
        result.pop()
    return ",".join(result)


def deserialize(data):
    """
    Deserialize string back into a binary tree.
    """
    if not data:
        return None
    values = data.split(",")
    root = TreeNode(int(values[0]))
    queue = deque([root])
    i = 1
    while queue and i < len(values):
        node = queue.popleft()
        if values[i] != "null":
            node.left = TreeNode(int(values[i]))
            queue.append(node.left)
        i += 1
        if i < len(values) and values[i] != "null":
            node.right = TreeNode(int(values[i]))
            queue.append(node.right)
        i += 1
    return root


# -------------------------
# TEST EXAMPLES
# -------------------------

if __name__ == "__main__":
    """
    Example Binary Tree:
            1
           / \
          2   3
         / \   \
        4   5   6
    """

    root = TreeNode(1)
    root.left = TreeNode(2, TreeNode(4), TreeNode(5))
    root.right = TreeNode(3, None, TreeNode(6))

    print("Pre-order:", end=" ")
    pre_order(root)
    print("\nIn-order:", end=" ")
    in_order(root)
    print("\nPost-order:", end=" ")
    post_order(root)
    print("\nBFS:", end=" ")
    breadth_first(root)

    print("\nMax Depth:", max_depth(root))
    print("Min Depth:", min_depth(root))
    print("Count Nodes:", count_nodes(root))
    print("Is Balanced?", is_balanced(root))
    print("Diameter:", diameter(root))
    print("Is Symmetric?", is_symmetric(root))

    print("Has Path Sum 8?", has_path_sum(root, 8))
    print("Has Path Sum 20?", has_path_sum(root, 20))

    print("Serialize:", serialize(root))
    new_root = deserialize(serialize(root))
    print("Deserialize BFS:", end=" ")
    breadth_first(new_root)
