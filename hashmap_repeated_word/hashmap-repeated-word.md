# challenge 31
# HashMap

## Challenge Type: ` Code Challenge / Algorithm`


## [Code](hashmap-repeated-word.py)
## [tests](../tests/test_hash_map.py)


## Challenge

Write a function called repeated word that finds the first word to occur more than once in a string
Arguments: string
Return: string

## Whiteboard Process
[Whiteboard](CC31.jpg)

## Approach & Efficiency
We tried to keep our code as simple as possible to the best performance by reducing space/Time complexity
so we end with the following:

### Big(O):
- Space: O(1) (space is constant in relation to input)
- Time: O(n) (time is dependent on the number of elements that we need to traverse)


## Solution

1. def a  repeated_word function which take a string as argument.
2. define the valid characters (Alphabetical ) to loop through them.
3. define variable that loop through the characters and make them lower case.
4. we use hashmap contain method  to check for the first repeated word.
5. return the value  repeated word as string
6. if there's no repeated word raise and error and handle it.

>The code have test folder so you can run 
> >**`pytest .\tests\test_hash_map.py`** 