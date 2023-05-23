 # stacks and Queues
- Create a Stack class that has a top property. It creates an empty Stack when instantiated.
  - This object should be aware of a default empty value assigned to top when the stack is created.
  - The class should contain the following methods:
    - push
    - pop
    - peek
    - is empty


- Create a Queue class that has a front property. It creates an empty Queue when instantiated.
  - This object should be aware of a default empty value assigned to front when the queue is created.
  - The class should contain the following methods:
     - enqueue
     - dequeue
     - peek
     - is empty

## Approach & Efficiency

### Stack:
 - method called push which takes any value as an argument and adds a new node with that value to the top of the stack with an O(1) Time performance.
 - method called pop that does not take any argument, removes the node from the top of the stack, and returns the node’s value.
 - Define a method called peek that does not take an argument and returns the value of the node located on top of the stack, without removing it from the stack.
 - method called isEmpty that takes no argument, and returns a boolean indicating whether or not the stack is empty.
### Queue:
 - Define a method called enqueue which takes any value as an argument and adds a new node with that value to the back of the queue with an O(1) Time performance.
 - Define a method called dequeue that does not take any argument, removes the node from the front of the queue, and returns the node’s value.
 - Define a method called peek that does not take an argument and returns the value of the node located in the front of the queue, without removing it from the queue.
 - Define a method called isEmpty that takes no argument, and returns a boolean indicating whether or not the queue is empty.

## Solution

- python stack_and_queue.py

 -Pytest

[Code link](stack_and_queue.py)<br>
[Test Code](../tests/test_stack_queue.py)<br>
[Pull link](https://github.com/WalaaAlrefai/data-structures-and-algorithms/pull/19)
