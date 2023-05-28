class Node:

    # Space: O(1)
    # Time: O(1)
    def __init__(self, value, next = None):
        self.value = value
        self.next = next


class Stack:

    # Space: O(1)
    # Time: O(1)
    def __init__(self, node=None):
        self.top = node


    # Space: O(N)
    # Time: O(1)
    def push(self, value):
        node = Node(value)
        node.next = self.top
        self.top = node

    # Space: O(1)
    # Time: O(1)
    def pop (self):
        if self.is_empty():
            raise BaseException("The stack is empty")
        else:
           node = self.top
           self.top = self.top.next
           return node.value

    # Space: O(1)
    # Time: O(1)
    def peek(self):
        if self.is_empty():
            raise BaseException("The stack is empty")
        return self.top.value

    # Space: O(1)
    # Time: O(1)
    def is_empty(self):
        return self.top == None

    def __str__(self):
        current = self.top
        items = ''

        while current:
            items += str(current.value)
            current = current.next

        return items


class Queue():

    # Space: O(1)
    # Time: O(1)
    def __init__(self, front=None):
        self.front = front
        self.back = None

    # Space: O(N)
    # Time: O(1)
    def enqueue(self, value):
        node = Node(value)
        if self.is_empty():
            self.front = node
            self.back = node
        else:
            self.back.next = node
            self.back = node

    # Space: O(1)
    # Time: O(1)
    def dequeue(self):
        if self.is_empty():
            raise BaseException("The stack is empty")
        temp = self.front
        self.front = self.front.next
        return temp.value

    # Space: O(1)
    # Time: O(1)
    def peek(self):
        if self.is_empty():
            raise BaseException("The stack is empty")
        return self.front.value

    # Space: O(1)
    # Time: O(1)
    def is_empty(self):
        return self.front == None

    def __str__(self):
        current = self.front
        items = ''
        while current:
            items += f"{current.value}"
            current = current.next

        return items
    

class PseudoQueue():
    def __init__(self):
        self.s1=Stack()
        self.s2=Stack()


    def enqueue(self,value):
        self.s1.push(value)


    def dequeue(self):
        while not self.s1.is_empty():
            val=self.s1.pop()
            self.s2.push(val)
        return self.s2.pop()
    
    def __str__(self):
        current = self.s1.top
        items = ''
        while current:
            items += f"<-{{{current.value}}}"
            current = current.next

        return "None"+items




if __name__=="__main__":

 queue_1 = PseudoQueue()
 queue_1.enqueue(1)
 queue_1.enqueue(2)
 queue_1.enqueue(3)
 queue_1.enqueue(4)

 print(queue_1)
 queue_2= PseudoQueue()
 queue_2.enqueue(1)
 queue_2.enqueue(2)
 queue_2.enqueue(3)
 queue_2.enqueue(4)
 queue_2.dequeue()
 queue_2.dequeue()
#  queue_2.dequeue()

 print(queue_2)