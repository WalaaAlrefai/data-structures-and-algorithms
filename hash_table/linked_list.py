class Node:

    def __init__(self, value, next=None):
        """
        This is the Node Constructor

        Arguments: value (value that the node represents) and next (optional param that defaults to none and represents the next node in the list).
        """
        self.value = value
        self.next = next



class LinkedList:

    def __init__(self, head=None):

        """ This is the constructor for the actual linked list.

        Arguments: head (optional param that defaults to none and represents the head of the linked list)."""
        
        self.head=head

    def insert(self,value):

        """
        Insert a value to the head of the linked list.

        Arguments: value (value that the new node represents)
        """
        node = Node(value)
        if self.head is not None:

            node.next = self.head

        self.head = node

    def includes(self,value):
        """
        Search the linked list for a specific value.

        Arguments: value (value we are searching for in the list).

        Output: A boolean (true of false).
        """

        current = self.head

        while current is not None:
            if current.value == value:
                return True

            current = current.next

        return False
    

    def __str__(self):
        """
        Produce a string representation of the linked list.

        Output: String representation of the linked list.
        """

        current = self.head
        string = ''

        while current is not None:
            string += f"{{{current.value}}}->"
            current = current.next

        return string + 'None'
    
    def append(self, value):
        """
        Appends value to end of linked list
        Arguments: value (value we trying to append).
        """
        node = Node(value)
        current = self.head
        if self.head == None:
            self.head = node
            return

        while current.next is not None:
            current = current.next

        current.next = node


    def insert_before(self,value,new_value):
        """
        Insert a new_value before the given value of linked list
        Arguments: two values (value for search , value we trying to insert).
        """

        current=self.head
        if current.value == value :
            self.insert(new_value)
            return
        
        while current is not None:
           if current.next.value == value :
               node = Node(new_value)
               node.next = current.next
               current.next = node

               return
           current=current.next


    def insert_after(self,value,new_value):
        """
        Insert a new_value after the given value of linked list
        Arguments: two values (value for search , value we trying to insert).
        """

        current=self.head
        if current.next.value == value :
            self.insert(new_value)
            return
        
        while current is not None:
           if current.value == value :
               node = Node(new_value)
               node.next = current.next
               current.next = node

               return
           current=current.next


    def kthFromEnd(self, k: int) -> int:
        """
        Gets the kth value from the end where the last node in the linked list has an index of 0.
         Increments by one with each traversal to the left.
        Arguments: k, which is an integer representing the number of elements from the end.
        """
        current = self.head
        list_counter = []
        while current is not None:
            list_counter.append(current)
            current = current.next
        list_size = len(list_counter)
        if k < list_size:
            return list_counter[list_size - (k+1) ].value
        else:
         raise Exception('There is no value at that index!')
    
        

def check_palindrome(list):
        current = list.head
        values = []
        result = True
        while current :
            values.append(current.value)
            current = current.next
        x, y = 0,-1
        for i in range(len(values)//2):
            if values[x] == values[y]:
                result = True
            else :
                result = False
                return result
            x+=1
            y-=1
        return result


def reverse_linked_list(ll):
        current = ll.head
        previous = None
        while current:
          next_node = current.next
          current.next = previous
          previous = current
          current = next_node
          reversed_ll = LinkedList()
          reversed_ll.head = previous
        return reversed_ll


# def palindrome(ll):
#         def helper(ll):
        
#          current = ll.head
#          previous = None
#          while current:
#            next_node = current.next
#            current.next = previous
#            previous = current
#            current = next_node
#            reversed_ll = LinkedList()
#            reversed_ll.head = previous
#          return reversed_ll
        
#         if helper(ll)==ll:
#             return True
#         else:
#             return False


def is_palindrome(ll):
    def reverse(head):
     previous = None
     current = head
     while current:
        next_node = current.next
        current.next = previous
        previous = current
        current = next_node
     return previous
    # Reverse the second half of the linked list
    
    slow = fast = ll.head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

    reversed_second_half = reverse(slow)

    # Compare the first half of the linked list with the reversed second half
    current1 = ll.head
    current2 = reversed_second_half
    while current1 and current2:
        if current1.value != current2.value:
            return False
        current1 = current1.next
        current2 = current2.next

    return True

def reverse(head):
    previous = None
    current = head
    while current:
        next_node = current.next
        current.next = previous
        previous = current
        current = next_node
    return previous

def palindrome(ll):
    def helper(ll):
        print (222222,ll)
        return ll

    def reverse(ll):
        current = ll.head
        previous = None
        while current:
            next_node = current.next
            current.next = previous
            previous = current
            current = next_node
        reversed_ll = LinkedList()
        reversed_ll.head = previous
        print (111111,reversed_ll)
        return reversed_ll

    if helper(ll) == reverse(ll):
        return True
    else:
        return False



if __name__=="__main__":
    ll = LinkedList()
    ll2 = LinkedList()
    ll.insert(10)
    ll.insert(11)
    ll.insert(12)
    ll.insert(13)
    ll.insert(14)
    ll.insert(15)
    print (ll)
    print(ll.includes(3))
    print(ll.includes(11))
    ll.append(9)
    ll.append(8)
    ll.append(7)
    ll.append(5)
    print(ll)
    ll.insert_before(5,6)
    print(ll)
    ll.insert_after(5,4)
    ll.insert_after(15,14.5)
    ll.insert_after(13,14.5)
    print(ll)
    print(reverse_linked_list(ll))
    print(palindrome(ll))
    ll2.insert("a")
    ll2.insert("b")
    ll2.insert("c")
    ll2.insert("b")
    ll2.insert("a")
    ll3=LinkedList()
    ll3.insert("l")
    ll3.insert("b")
    ll3.insert("m")
    ll3.insert("b")
    ll3.insert("a")
    
    print(is_palindrome(ll2))
    print(is_palindrome(ll3))