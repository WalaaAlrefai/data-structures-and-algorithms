
## stack-queue-pseudo

[Code](stack_queue_pseudo.py)<br>
[tests](../tests/test_queue_pseudo.py)

## Challenge11
Create a brand new PseudoQueue class. Do not use an existing Queue. Instead, this PseudoQueue class will implement our standard queue interface (the two methods listed below), but will internally only utilize 2 Stack objects. Ensure that you create your class with the following methods:

- enqueue(value) which inserts value into the PseudoQueue, using a first-in, first-out approach.

- dequeue() which extracts a value from the PseudoQueue, using a first-in, first-out approach.

## Whiteboard Process

![WhiteBoard](Untitled%20(11).jpg)


## Approach & Efficiency
For the two methods we write them as simple as possible so we can keep the complextiy as samll as possible.

### Enqueue
Space: O(1)
Time: O(1)
### Dequeue
Space: O(n)
Time: O(n)