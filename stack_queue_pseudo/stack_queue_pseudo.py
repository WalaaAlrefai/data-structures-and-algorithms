from stack_and_queue.stack_and_queue import Stack, Node


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


if __name__ == "__main__":

 queue_1 = PseudoQueue()
 queue_1.enqueue(1)
 queue_1.enqueue(2)
 queue_1.enqueue(3)
 queue_1.enqueue(4)

 print(queue_1)