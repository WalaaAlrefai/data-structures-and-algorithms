# Hash Tables

## Challenge 30 

## [Code](hash_table.py)
## [tests](../tests/test_hash_table.py)


## Challenge

Implement a Hashtable Class with the following methods:
- set 
- get
- contains
- keys
- hash

The code should do the next functionality:

1. Setting a key/value to your hashtable results in the value being in the data structure
2. Retrieving based on a key returns the value stored
3. Successfully returns null for a key that does not exist in the hashtable
4. Successfully returns a list of all unique keys that exist in the hashtable
5. Successfully handle a collision within the hashtable
6. Successfully retrieve a value from a bucket within the hashtable that has a collision
7. Successfully hash a key to an in-range value

## Approach & Efficiency
- All of the methods above exist in the Hashtable class.
- The hash table is instantiated with 1024 buckets that have a default value of None.
- Collisions are handled with the linked list data structure.

### Big O:
the following table will show Big(O) for each method

| **Method** | **Time** | **Space** |
|------------|----------|-----------|
| hash       | O(1)     | O(1)      |
| set        | O(1)     | O(1)      |
| get        | O(n)     | O(n)      |
| has    | O(n)     | O(n)      |
| keys        | O(n)     | O(n)      |



