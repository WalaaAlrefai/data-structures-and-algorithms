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
           temp = self.top
           self.top = temp.next
           temp.next=None
           return temp.value

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
            items +=f"{current.value} -> "
            current = current.next
         
        return items +"None"


class Queue:

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
        self.front = temp.next
        temp.next=None
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
            items += f"{current.value} ->"
            current = current.next

        return items+"None"
    

if __name__=="__main__" :
    stack_01 =Stack()
    stack_01.push(1)
    stack_01.push(2)
    stack_01.push(3)
    stack_01.push(4)
    print (stack_01)
    print (stack_01.top.value)
    print (stack_01.is_empty())
    stack_02=Stack()
    print (stack_02.is_empty())
    stack_01.push(5)
    print (stack_01)
    print(stack_01.pop())
    print (stack_01)


