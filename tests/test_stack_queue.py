import pytest
from stack_and_queue.stack_and_queue import Node, Stack, Queue

def test_new_empty_stack():
    stack = Stack()
    actual = stack.top
    expected = None
    assert actual == expected

def test_push_once():
    stack = Stack()
    stack.push(1)
    actual = stack.top.value
    expected = 1
    assert actual == expected

def test_push_multi_time():
    stack = Stack()
    stack.push(1)
    stack.push(2)
    stack.push(3)
    actual = stack.top.value
    expected = 3
    assert actual == expected

def test_pop_once():
    stack = Stack()
    stack.push(1)
    actual = stack.pop()
    expected = 1
    assert actual == expected

def test_pop_until_empty():
    stack = Stack()
    stack.push(1)
    stack.push(2)
    stack.push(3)
    stack.pop()
    stack.pop()
    stack.pop()
    actual = stack.is_empty()
    expected = True
    assert actual == expected

def test_peek_one():
  stack = Stack()
  stack.push(1)
  stack.push(2)
  actual = stack.peek()
  expected = 2
  assert actual == expected

def test_is_not_empty():
    stack = Stack()
    stack.push(1)
    stack.push(2)
    actual = stack.is_empty()
    expected = False
    assert actual == expected

def test_is_empty_while_peek():
    stack = Stack()
    with pytest.raises(BaseException) as e:
        stack.peek()
    assert str(e.value) == "The stack is empty"

def test_is_empty_while_pop():
    stack = Stack()
    with pytest.raises(BaseException) as e:
        stack.pop()
    assert str(e.value) == "The stack is empty"

def test_enqueue():
    qeueue = Queue()
    qeueue.enqueue(1)
    actual = qeueue.front.value
    expected = 1
    assert actual == expected

def test_enqueue_many():
    qeueue = Queue()
    qeueue.enqueue(1)
    qeueue.enqueue(2)
    qeueue.enqueue(3)
    actual = qeueue.front.value
    expected = 1
    assert actual == expected

def test_dequeue():
    queue = Queue()
    queue.enqueue(1)
    queue.enqueue(2)
    actual = queue.dequeue()
    expected = 1
    assert actual == expected



def test_dequeue_untill_empty():
    queue = Queue()
    queue.enqueue(1)
    queue.enqueue(2)
    queue.enqueue(3)
    queue.dequeue()
    queue.dequeue()
    queue.dequeue()
    actual = queue.is_empty()
    expected = True
    assert actual == expected

def test_peek_once():
    queue = Queue()
    queue.enqueue(1)
    actual = queue.peek()
    expected = 1
    assert actual == expected

# peek into a queue
def test_peek():
    queue = Queue()
    queue.enqueue(1)
    queue.enqueue(2)
    queue.enqueue(3)
    actual = queue.peek()
    expected = 1
    assert actual == expected

# instantiate an empty queue
def test_is_not_empty_queue():
    queue = Queue()
    queue.enqueue(1)
    queue.enqueue(2)
    actual = queue.is_empty()
    expected = False
    assert actual == expected

# Calling dequeue on empty queue raises exception
def test_is_empty_while_dequeue():
    queue = Queue()
    with pytest.raises(BaseException) as e:
        queue.dequeue()

    assert str(e.value) == "The stack is empty"

# Calling peek on empty queue raises exception
def test_is_empty_while_queue_peek():
    queue = Queue()
    with pytest.raises(BaseException) as e:
        queue.peek()

    assert str(e.value) == "The stack is empty"
