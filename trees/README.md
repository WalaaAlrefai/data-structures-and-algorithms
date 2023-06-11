# Challenge 15
## Trees

Create three classes, Node, BinaryTree, and BinarySearchTree. Using test-driven development, implement/test the following features:

- Can successfully instantiate an empty tree
- Can successfully instantiate a tree with a single root node
- Can successfully add a left child and right child to a single root node
- Can successfully return a collection from a preorder traversal
- Can successfully return a collection from an inorder traversal
- Can successfully return a collection from a postorder traversal
- Returns true false for the contains method, given an existing or non-existing node value
## Whiteboard Process
NO WHITEBOARD FOR THIS CODE CHALLENGE.

## Approach & Efficiency
We tried to keep our code as simple as possible to the best performance by reducing space/Time complexity so we end with the following

## Big O:

Time complexity => O(N) for both adding a new node and searching for a specific node using recursive.
Space complexity => O(N) for a node addition only, and O(1) for the contains method

## solution
[Code](trees.py) <br>
[Test](../tests/test_trees.py)