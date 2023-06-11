import pytest
from trees.trees import TNode, BinaryTree,BinarySearchTree


# Instantiate empty tree
def test_empty_tree():
    tree = BinaryTree()
    assert tree.root == None

# instantiate tree  single root node
def test_single_root_tree():
     root_node = "A"
     tree = BinaryTree(root_node)
     assert tree.root == root_node

# For a Binary Search Tree, can successfully add a left child and right child properly to a node
def test_left_right_child_tree():
     root_node = BinaryTree(1)
     bst = BinarySearchTree(root_node)
     bst.root.left = 0
     bst.root.right = 2
     assert bst.root.left == 0 and bst.root.right == 2

# return array from pre_order traversal
def test_bts_pre_order(test_tree):
    actual = test_tree.pre_order()
    expected = ["A","B","D","E", "C","F"]
    assert actual == expected


# return array from in_order traversal
def test_bts_in_order(test_tree):
    actual = test_tree.in_order()
    expected = ["D", "B" ,"E" ,"A", "F", "C"]
    assert actual == expected


# return array from post_order traversal
def test_bts_post_order(test_tree):
    actual = test_tree.post_order()
    expected = ["D", "E", "B", "F", "C", "A"]
    assert actual == expected

# Binary Search Tree add values
def test_success_add_node_to_bst(test_bst):
    test_bst.add(13)
    test_bst.add(23)
    assert test_bst.root.left.right.value == 13
    assert test_bst.root.right.left.left.value == 23

# Binary Search Tree contains  values
def test_success_bst_contains_value(test_bst):
    assert test_bst.contains(24) == True
    assert test_bst.contains(60) == False
    assert test_bst.contains(36) == True


# Find the Maximum Value in a Binary Tree
def test_find_maxval_bt(test_tree):
  expected = "F"
  actual = test_tree.max_tree()
  assert actual == expected



@pytest.fixture
def test_tree():

    tree = BinaryTree()

    one = TNode("A")
    two = TNode("B")
    three = TNode("C")
    four = TNode("D")
    five = TNode("E")
    six = TNode("F")
    #seven = TNode("G")

    tree.root = one
    one.left = two
    one.right = three
    two.left = four
    two.right = five
    three.left = six
    #three.right = seven

    return tree

@pytest.fixture
def test_bst():

    tree = BinaryTree()
    bst = BinarySearchTree(tree)

    one = TNode(15)
    two = TNode(12)
    three = TNode(25)
    four = TNode(24)
    five = TNode(29)
    six = TNode(36)

    bst.root = one
    one.left = two
    one.right = three
    three.left = four
    three.right = five
    five.right = six

    return bst