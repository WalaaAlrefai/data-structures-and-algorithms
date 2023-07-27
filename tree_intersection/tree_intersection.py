from trees.trees import BinaryTree,TNode
from hash_table.hash_table import Hashtable

def tree_intersection(tree_1,tree_2):
    """
    function called tree_intersection that takes two binary trees as parameters.
 Using your Hashmap implementation as a part of your algorithm, return a set of values found in both trees.
Arguments: two binary trees
Return: set of values found in both trees.
    """
    common = []
    binary_tree1 = tree_1.pre_order()
    binary_tree2 = tree_2.pre_order()
    hashtable = Hashtable()

    for value in binary_tree1:
        hashtable.set(key=str(value), value=value)
    for value in binary_tree2:
        if hashtable.has(str(value)):
            common.append(value)
    return common

tree = BinaryTree()
    # tree = BinarySearchTree()
tree.root = TNode(2)
tree.root.left = TNode(5)
tree.root.right = TNode(7)
tree.root.left.left = TNode(2)
tree.root.left.right = TNode(6)
tree.root.right.right = TNode(8)
tree.root.right.left = TNode(9)
tree.root.right.right.right = TNode(4)
tree.root.right.right.right.right = TNode(7)
tree.root.right.right.right.right.right = TNode(15)

tree2 = BinaryTree()
    # tree = BinarySearchTree()
tree2.root = TNode(2)
tree2.root.left = TNode(7)
tree2.root.right = TNode(12)
tree2.root.left.left = TNode(3)
tree2.root.left.right = TNode(14)
tree2.root.right.right = TNode(8)

print(tree_intersection(tree,tree2))