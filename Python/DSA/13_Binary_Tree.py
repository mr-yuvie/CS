# This also includes Binary Search Tree
class TreeNode:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None


# Creating Nodes
node0 = TreeNode(2)
node1 = TreeNode(1)
node2 = TreeNode(3)
root = node0

# Connecting Nodes
node0.left = node1
node0.right = node2

# Creating a much more complicated tree [(left_value, root, right_value )]
tree_tuple_1 = ((-1, 1, None), 2, ((None, 3, 4), 5, (6, 7, 8)))


def Tree_Using_Tuple(data):
    if isinstance(data, tuple) and len(data) == 3:
        node = TreeNode(data[1])
        node.left = Tree_Using_Tuple(data[0])
        node.right = Tree_Using_Tuple(data[2])
    elif data is None:
        node = None
    else:
        node = TreeNode(data)
    return node


tree_1 = Tree_Using_Tuple(tree_tuple_1)


# The Display has to be rotated 90 degree
def Display_Keys(node, space="\t", level=0):
    # If the node is empty
    if node is None:
        print(space * level + "@")  # @:Represets None values
        return

    # If the node is a leaf
    if (node.left is None) and (node.right is None):
        print(space * level + str(node.key))
        return

    # If the node has children
    Display_Keys(node.right, space, level + 1)
    print(space * level + str(node.key))
    Display_Keys(node.left, space, level + 1)


# Display_Keys(tree_1)


def Traverse_In_Order(node):
    if node is None:
        return []
    return Traverse_In_Order(node.left) + [node.key] + Traverse_In_Order(node.right)


# print(Traverse_In_Order(tree_1))


# Longest Path in the Tree
def Tree_Height(node):
    if node is None:
        return 0
    return 1 + max(Tree_Height(node.left), Tree_Height(node.right))


# print(Tree_Height(tree_1))


def Tree_Size(node):
    if node is None:
        return 0
    return 1 + Tree_Size(node.left) + Tree_Size(node.right)


# print(Tree_Size(tree_1))

## Binary Search Tree: A tree with smaller values than root on left and larger values than root on right
# Write a function to check if a binary tree is a binary search tree
# Write a function to find maximum key in a binary tree
# Write a function to find minimum key in a binary tree


def Remove_None(nums):
    return [x for x in nums if x is not None]


def Is_BST(node):
    if node is None:
        return True, None, None

    Is_BST_L, Min_L, Max_L = Is_BST(node.left)
    Is_BST_R, Min_R, Max_R = Is_BST(node.right)

    Is_BST_node = (
        Is_BST_L
        and Is_BST_R
        and (Max_L is None or node.key > Max_L)
        and (Min_R is None or node.key < Min_R)
    )
    Min_Key = min(Remove_None([Min_L, node.key, Min_R]))
    Max_Key = max(Remove_None([Max_L, node.key, Max_R]))

    return Is_BST_node, Min_Key, Max_Key


# print(Is_BST(tree_1))


# Insertion into BST
def Insert(node, key):
    if node is None:
        node = TreeNode(key)
    elif key < node.key:
        node.left = Insert(node.left, key)
    elif key > node.key:
        node.right = Insert(node.right, key)
    return node


# Insertion Order matters else you can end up with a Skewed Tree
# Insert(tree_1, 9)
# Display_Keys(tree_1)

tree_tuple_2 = ((None, 9, None), 14, ((None, 17, 19), 21, (22, 25, 34)))
tree_2 = Tree_Using_Tuple(tree_tuple_2)

# print(Is_BST(tree_2))
# Display_Keys(tree_2)

# Insert(tree_2, 11)
# Display_Keys(tree_2)


# Finding a Node
def Find_Node(node, key):
    if node is None:
        return None
    if key == node.key:
        return node
    if key < node.key:
        return Find_Node(node.left, key)
    elif key > node.key:
        return Find_Node(node.right, key)


# node = Find_Node(tree_2, 34)
# print(node)
# print(node.key)

# node = Find_Node(tree_2, 15)
# print(node)


# You can't delete root node
def Delete_Node(node, key):
    if node is None:
        return None
    if key == node.left.key:
        node.left = None
        return
    if key == node.right.key:
        node.right = None
        return
    if key < node.key:
        return Delete_Node(node.left, key)
    elif key > node.key:
        return Delete_Node(node.right, key)


# Delete_Node(tree_2, 34)
# Display_Keys(tree_2)
# print(Traverse_In_Order(tree_2))

# Insert(tree_2,34)
# Display_Keys(tree_2)

# Delete_Node(tree_2, 25)
# Display_Keys(tree_2)

# Insert(tree_2, 25)
# Insert(tree_2, 34)
# Insert(tree_2, 22)
# Display_Keys(tree_2)
