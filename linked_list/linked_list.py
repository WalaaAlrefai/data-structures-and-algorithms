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
    
    def insert_after(self,value,new_value):
        """
        Insert a new_value after the given value of linked list
        Arguments: two values (value for search , value we trying to insert).
        """

        current=self.head
        while current is not None:
           if current.value == value :
               node = Node(new_value)
               node.next = current.next
               current.next = node

               return
           current=current.next

           

    

if __name__=="__main__":
    ll = LinkedList()
    ll.insert(10)
    ll.insert(11)
    ll.insert(12)
    ll.insert(13)
    ll.insert(14)
    ll.insert(15)
    print (ll)
    print(ll.includes(3))
    print(ll.includes(11))

    ll.insert_after(12,8)
    print(ll)