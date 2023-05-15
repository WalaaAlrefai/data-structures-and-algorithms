from linked_list.linked_list import LinkedList, Node
import pytest

# def test_import():
#     assert LinkedList


# Test empty linked list inistantiation
# it should return none
def test_empty_list():
    actual = LinkedList().head
    expected = None
    assert actual == expected


  # Test inserting node into linked list
  # it return nothing but add the node to the head of linked list
def test_insert_in_list():
    link_list = LinkedList()
    link_list.insert(75)
    actual = link_list.head.value
    expected = 75
    assert actual == expected


# Testing head points (->) to first node
# checks if the head is points at the firtt node in the list
def test_list_head():
    node = Node(45)
    actual = LinkedList(node).head
    expected = node
    assert actual == expected

# checks if it can added multible nodes to the head of our linked list
def test_insert_multiple_nodes():
    val1 = 'Ibrahim'
    val2 = 'Walaa'
    val3 = 'Tamim'
    val4 = 'Julia'
    linked_list = LinkedList(val1)
    linked_list.insert(val2)
    linked_list.insert(val3)
    linked_list.insert(val4)
    actual = linked_list.head.value
    expected = 'Julia'
    assert actual == expected



# Testing False for includes
# checks if it return false
def test_if_list_includes_two():
    node = Node(50)
    actual = LinkedList(node).includes(49)
    expected = False
    assert actual == expected


# Testing True for includes
# checks if it return True
def test_list_includes_onehundred():
    node = Node(100)
    actual = LinkedList(node).includes(100)
    expected = True
    assert actual == expected


# Testing the string method
# return the list in " {node1}->{node2}->{node3}->none " shape
def test_linked_list_str():
    link_list = LinkedList()
    link_list.insert('c')
    link_list.insert('b')
    link_list.insert('a')
    actual = str(link_list)
    expected = "{a}->{b}->{c}->None"
    assert actual == expected