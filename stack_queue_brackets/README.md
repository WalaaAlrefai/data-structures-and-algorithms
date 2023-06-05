# Challenge 13
## Stack_Queue_brackets

Create a function that takes a string and returns true or false depending on whether or not the brackets ('{}', '[]', '()') are balanced.

## Whiteboard Process

![whiteborad](Untitled%20(13).jpg)

## Approach & Efficiency
Using a stack, I iterate through the string. The opening brackets are pushed onto the stack and then when a closing bracket is found, the corresponding opening bracket is popped out from the stack for comparing If the stacks ends up being empty at the end, return true.

BIG(O):

 - Space: O(N)
 - Time: O(N)

## Solution
[Code](stack_queue_brackets.py)<br>
[test](../tests/test_stack_brackets.py)