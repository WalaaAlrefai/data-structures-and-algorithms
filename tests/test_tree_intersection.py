from tree_intersection.tree_intersection import tree_intersection
from trees.trees import BinaryTree, TNode
import pytest


def test_tree_instance():
    bt = BinaryTree()
    assert bt


def test_TNode_instance():
    node = TNode(tree_1)
    tree = BinaryTree()
    assert node
    assert tree


def test_tree_commons(tree_1, tree_2):
    actual = tree_intersection(tree_1, tree_2)
    expected = [1, 13]
    assert actual == expected


def test_tree_no_commons(tree_1, tree_3):
    actual = tree_intersection(tree_1, tree_3)
    expected = []
    assert actual == expected


@pytest.fixture
def tree_1():
    tree1 = BinaryTree()
    tree1.root = TNode(1)
    tree1.root.left = TNode(3)
    tree1.root.right = TNode(5)
    tree1.root.left.left = TNode(7)
    tree1.root.left.right = TNode(9)
    tree1.root.right.left = TNode(11)
    tree1.root.right.right = TNode(13)
    return tree1


@pytest.fixture
def tree_2():
    tree2 = BinaryTree()
    tree2.root = TNode(1)
    tree2.root.left = TNode(4)
    tree2.root.right = TNode(6)
    tree2.root.left.left = TNode(8)
    tree2.root.left.right = TNode(10)
    tree2.root.right.left = TNode(12)
    tree2.root.right.right = TNode(13)
    return tree2


@pytest.fixture
def tree_3():
    tree3 = BinaryTree()
    tree3.root = TNode(14)
    return tree3