# from stack_and_queue.stack_and_queue import Stack

class MaxStackNode:

    """
        class used to represent a node in the linked list
        used by the MaxStack class. Each MaxStackNode object holds a value and 
        a reference to the next node in the linked list.
    """
    
    def __init__(self, value): 
        self.value = value
        self.next = None


class MaxStack:

    """
        'Max Stack' class, which is a stack with an additional getMax() 
        member function that returns the 'biggest' element in the stack. 
    """
    def __init__(self):
        self.top = None
        self.maxStack = []

    def push(self, value):
        new_node = MaxStackNode(value)

        if self.top is None:
            self.top = new_node
            self.maxStack.append(value)
        else:
            new_node.next = self.top
            self.top = new_node

            if value >= self.maxStack[-1]:
                self.maxStack.append(value)    
    def __str__(self):
        current = self.top
        string = ''

        while current is not None:
            string += f"{{{current.value}}}->"
            current = current.next

        return string + 'None'
    

    def pop(self):
        if self.top is None:
            return None

        popped_value = self.top.value
        self.top = self.top.next

        if popped_value == self.maxStack[-1]:
            self.maxStack.pop()

        return popped_value

    def getMax(self):
        '''
        getMax() member function that returns the 'biggest' element in the stack
        '''
        if self.top is None:
            return None

        return self.maxStack[-1]
    



print("hello")
m_stack= MaxStack()
m_stack.push(1)
m_stack.push(5)
m_stack.push(3)
m_stack.push(-8)
m_stack.push(4)
print(m_stack)
print(m_stack.getMax()) 


stack = MaxStack()
stack.push(5)
stack.push(10)
stack.push(7)
print(stack)

print(stack.getMax())  # Output: 10

stack.pop()
print(stack)
print(stack.getMax())  # Output: 10

stack.pop()
print(stack)
print(stack.getMax())  # Output: 5
    


