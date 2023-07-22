from hash_table.hash_table import Hashtable
from linked_list.linked_list import Node, LinkedList


def test_create():
    hashtable = Hashtable()
    assert hashtable


def test_predictable_hash():
    hashtable = Hashtable()
    initial = hashtable._hash('ok')
    secondary = hashtable._hash('ok')
    assert initial == secondary


def test_same_hash():
    hashtable = Hashtable()
    initial = hashtable._hash('key_1')
    secondary = hashtable._hash('1_key')
    assert initial == secondary


def test_different_hash():
    hashtable = Hashtable()
    initial = hashtable._hash('key_1')
    secondary = hashtable._hash('key_2')
    assert initial != secondary


# Adding a key/value to your hashtable results in the value being in the data structure
def test_adding_keyval_pair():
    hashtable = Hashtable()
    hashtable.set('key_1', 'One')
    actual = hashtable.has('key_1')
    expected = True
    assert actual == expected


# Retrieving based on a key returns the value stored
def test_retrieving_value_from_key():
    hashtable = Hashtable()
    hashtable.set('key_1', 'One')
    actual = hashtable.get('key_1')
    expected = 'One'
    assert actual == expected


# Successfully returns False for a key that does not exist in the hashtable
def test_key_that_does_not_exist():
    hashtable = Hashtable()
    hashtable.set('key_1', 'One')
    actual = hashtable.has('key_2')
    expected = False
    assert actual == expected

# Successfully returns a list of all unique keys that exist in the hashtable
def test_returns_a_list_of_all_unique_keys():
    hashtable = Hashtable()
    hashtable.set('key_1', 'One')
    hashtable.set('key_2', 'One')
    hashtable.set('key_3', 'One')
    actual = hashtable.keys()
    expected = ['key_1', 'key_2', 'key_3']
    assert actual == expected

# Successfully handle a collision within the hashtable
def test_hashtable_collision():
    hashtable = Hashtable()
    initial = hashtable.set('key_1', 'One')
    secondary = hashtable.set('1_key', 'Two')
    assert hashtable._hash('key_1') == hashtable._hash('1_key')


# Successfully retrieve a value from a bucket within the hastable that has a collision
def test_retrieve_value_in_collision_bucket():
    hashtable = Hashtable()
    initial = hashtable.set('key_1', 'One')
    secondary = hashtable.set('key_2', 'Two')
    actual = hashtable.get('key_2')
    expected = 'Two'
    assert actual == expected


# Successfully hash a key to an in-range value
def test_in_range_hash():
    hashtable = Hashtable()
    actual = hashtable._hash('ok')
    assert 0 <= actual < hashtable._size