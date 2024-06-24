class TreeNode:
    def __init__(self, key):
        self.key = key
        self.left = None  # Pointer to the left child node
        self.right = None # Pointer to the right child node

# Create nodes
root = TreeNode(10)
left_child = TreeNode(5)
right_child = TreeNode(15)

# Connect nodes using child pointers
root.left = left_child
root.right = right_child

# Now the structure is:
#      10
#     /  \
#    5    15