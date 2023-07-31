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


# Add node to end of list
def test_append_node_to_list():
    link_list = LinkedList()
    link_list.insert('b')
    link_list.insert('c')
    link_list.append('a')
    actual = str(link_list)
    expected = "{c}->{b}->{a}->None"
    assert actual == expected

# Add multiple nodes to end of list
def test_append_nodes_to_list():
    link_list = LinkedList()
    link_list.insert('c')
    link_list.insert('d')
    link_list.append('b')
    link_list.append('a')
    actual = str(link_list)
    expected = "{d}->{c}->{b}->{a}->None"
    assert actual == expected

# insert before middle
def test_insert_before_middle():
    link_list = LinkedList()
    link_list.insert('c')
    link_list.insert('d')
    link_list.append('b')
    link_list.append('a')
    link_list.insert_before('b', 'middle')
    actual = str(link_list)
    expected = "{d}->{c}->{middle}->{b}->{a}->None"
    assert actual == expected


    # insert after middle
def test_insert_after_middle():
    link_list = LinkedList()
    link_list.insert('c')
    link_list.insert('d')
    link_list.append('b')
    link_list.append('a')
    link_list.insert_after('b', 'middle')
    actual = str(link_list)
    expected = "{d}->{c}->{b}->{middle}->{a}->None"
    assert actual == expected

# insert before first
def test_insert_before_first():
    link_list = LinkedList()
    link_list.insert('c')
    link_list.insert('d')
    link_list.append('b')
    link_list.append('a')
    link_list.insert_before('d', 'first')
    actual = str(link_list)
    expected = "{first}->{d}->{c}->{b}->{a}->None"
    assert actual == expected

# insert after last
def test_insert_after_last():
    link_list = LinkedList()
    link_list.insert('c')
    link_list.insert('d')
    link_list.append('b')
    link_list.append('a')
    link_list.insert_after('a', 'last')
    actual = str(link_list)
    expected = "{d}->{c}->{b}->{a}->{last}->None"
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


# Where k is greater than the length of the linked list
def test_kth_greater_than_len():
     link_list = LinkedList()
     link_list.insert(1)
     link_list.insert(2)
     link_list.insert(3)
     link_list.insert(4)
     with pytest.raises(Exception):
      link_list.kthFromEnd(5)
    
# k and the length of the list are the same
def test_kth_equal_to_ll_length():
    link_list = LinkedList()
    link_list.insert(1)
    link_list.insert(2)
    link_list.insert(3)
    link_list.insert(4)
    with pytest.raises(Exception):
        link_list.kthFromEnd(4)

# k is not a positive integer
def test_kth_negative():
    link_list = LinkedList()
    link_list.insert(1)
    link_list.insert(2)
    link_list.insert(3)
    link_list.insert(4)
    with pytest.raises(Exception):
        link_list.kthFromEnd(-4)

# LL has a size of 1
# def test_kth_size_one():
#     link_list = LinkedList()
#     link_list.insert(1)
#     actual = link_list.kthFromEnd(0)
#     expected = 1
#     assert actual == expected

# k is somewhere in the middle
# def test_kth_middle_value():
#     link_list = LinkedList()
#     link_list.insert(1)
#     link_list.insert(10)
#     link_list.insert(100)
#     link_list.insert(1000)
#     actual = link_list.kthFromEnd(2)
#     expected = 100
#     assert actual == expected
