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


    # def kthFromEnd(self, k: int) -> int:
    #     """
    #     Gets the kth value from the end where the last node in the linked list has an index of 0.
    #      Increments by one with each traversal to the left.
    #     Arguments: k, which is an integer representing the number of elements from the end.
    #     """
    #     current = self.head
    #     list_counter = []
    #     while current is not None:
    #         list_counter.append(current)
    #         current = current.next
    #     list_size = len(list_counter)
    #     if k < list_size:
    #         return list_counter[list_size - (k+1) ].value
    #     else:
    #      raise Exception('There is no value at that index!')
    def kthFromEnd(self, k: int) -> int:
        slow=fast=ll.head
        for i in range (k+1):
            fast=fast.next
        if not fast:
            return Exception('There is no value at that index!')
        while fast.next:
            slow=slow.next
            fast=fast.next

        slow=slow.next
        return slow.value
    


    def addTwoNumbers(self, ll1, ll2):
        l1=ll1.head
        l2=ll2.head
        dummyHead = Node(0)
        tail = dummyHead
        carry = 0

        while l1 is not None or l2 is not None or carry != 0:
            digit1 = l1.value if l1 is not None else 0
 
            digit2 = l2.value if l2 is not None else 0

            sum = digit1 + digit2 + carry
            digit = sum % 10
            carry = sum // 10
            newNode = Node(digit)
            tail.next = newNode
            tail = tail.next

            l1 = l1.next if l1 is not None else None
            l2 = l2.next if l2 is not None else None
        ll=LinkedList()  # to see the result
        ll.head = dummyHead.next #result
        dummyHead.next = None
        return ll #result
    
def remove_Nth_from_end(ll,n):
    slow=fast=ll.head         
    for i in range (n):
        fast=fast.next

    if not fast :
            return ll.head
    while fast.next :
        slow= slow.next
        fast=fast.next
    slow.next=slow.next.next
    remll=LinkedList() #result
    remll.head=ll.head #result
    return remll





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
          ll.head = previous
        return ll




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
        current1=current1.next
        current2=current2.next
    return True     
    


def swap_pairs(ll):
    dummy = Node(0)
    curr=ll.head
    dummy.next = ll.head
    prev = dummy

    while curr and curr.next:
        # Nodes to swap
        first_node = curr
        second_node = curr.next

        # Swapping
        prev.next = second_node
        first_node.next = second_node.next
        second_node.next = first_node

        # Move pointers forward
        prev = first_node
        curr = prev.next
    ll.head=dummy.next
    return ll

def merge_ll(ll1,ll2):
    curr1= ll1.head
    curr2=ll2.head
    pointer=dummy=Node(0)

    while curr1 and curr2:
        if curr1.value < curr2.value :
            pointer.next=curr1
            pointer=curr1
            curr1=curr1.next
        else :
            pointer.next=curr2
            pointer=curr2
            curr2=curr2.next
    if curr1 or curr2:
        pointer.next=curr1 if curr1 else curr2
    ll1.head= dummy.next
    return ll1

def deleteDuplicates(ll):
    dummyHead=Node(0)
    dummyHead.next=ll.head
    curr=ll.head
    previous=dummyHead

    while curr and curr.next:
        if curr.value == curr.next.value :
            while curr and curr.next and curr.value == curr.next.value:
                curr=curr.next
            curr=curr.next
            previous.next=curr
        else :
            curr=curr.next
            previous=previous.next
    ll.head=dummyHead.next
    return ll

def rotateRight(ll,k):
    if not ll.head or k==0:
        return ll.head
    length=1
    curr=ll.head
    while curr.next :
        curr=curr.next
        length+=1
    curr.next=ll.head
    k=length-(k%length)
    while k>0:
        curr=curr.next
        k-=1

    newhead = curr.next
    curr.next=None
    ll.head= newhead
    return ll
def removeElements(ll,val):

        dummyHead=Node(0)
        dummyHead.next=ll.head
        current=dummyHead
        while current.next :
            if current.next.value == val :
                current.next=current.next.next
            else:
                current=current.next
        ll.head= dummyHead.next
        return ll

if __name__=="__main__":
    ll = LinkedList()
    ll2 = LinkedList()
    ll.insert(1)
    ll.insert(2)
    ll.insert(3)
    ll.insert(14)
    ll.insert(5)
    ll.insert(6)
    print (ll)
    print(ll.includes(3))
    print(ll.includes(11))
    print("swaping",swap_pairs(ll))
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
    print(ll.kthFromEnd(3))
    print(reverse_linked_list(ll))
    print(ll.kthFromEnd(3))
    print(is_palindrome(ll))
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
    ll4=LinkedList()
    ll4.insert(1)
    ll4.insert(2)
    ll4.insert(3)
    
    
    print(is_palindrome(ll2))

    print(is_palindrome(ll3))
    print(ll)
    print(ll4)
    print(ll.addTwoNumbers(ll,ll4))
    print(remove_Nth_from_end(ll,2))
    ll5=LinkedList()
    ll5.append(1)
    ll5.append(2)
    ll5.append(4)
    ll6=LinkedList()
    ll6.append(1)
    ll6.append(4)
    ll6.append(4)
    print(merge_ll(ll5,ll6))
    print("ll5",ll5)
    print("ll6",ll6)
    print(deleteDuplicates(ll6))
    print(ll)
    print(rotateRight(ll,2))
    ll7=LinkedList()
    ll7.append(1)
    ll7.append(1)
    ll7.append(2)
    ll7.append(1)
    print(ll7)
    print(is_palindrome(ll7))
    print(ll)
    print(removeElements(ll,2))
    
    