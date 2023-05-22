## linked-list-zip
Code
tests
## Challenge08
 two linked lists as inputs, and we want to merge them together so that they alternate between values. If one list is longer than the other, start adding the extra values in order from the linked list that is longer than the other. Return a reference to head of zipped list.

## Whiteboard Process
[WhiteBoard](Untitled%20(9).jpg)

## Approach & Efficiency
define the head of both linkedlists. While those both have values, assign the next node for each in separate variables. Set the next of the first linkedlist's first value to the second linkedlist's first value and so on, until one  linkedlist runs out of nodes. In that case, the original sequence of the linkedlist with more nodes is continued until the end is reached. Utilized existing methods in the LinkedList class to test output. Time: O(n) Space: O(1).