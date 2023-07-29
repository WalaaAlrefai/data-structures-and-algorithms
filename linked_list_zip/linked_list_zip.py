from linked_list.linked_list import LinkedList, Node

def zip_Lists( list1, list2):
    """
    This function takes in two linked lists and merges them together.

    Input: Two linked lists

    Output: Merged linked list the alternates between values of the original two linked lists.
    """

    current1 = list1.head
    current2 = list2.head



    while current1 and current2:
        next1 = current1.next
        next2 = current2.next
        current1.next = current2
        current2.next = next1
        last_current1 = current1.next
        current1 = next1
        current2 = next2
        if not current2 and current1:
           last_current1.next = current1


    return list1


if __name__=="__main__":
    ll = LinkedList()
    ll2= LinkedList()
    ll.insert(10)
    ll.insert(11)
    ll.insert(12)
    ll.insert(13)
    ll.insert(14)
    ll.insert(15)
    ll2.insert("a")
    ll2.insert("b")
    ll2.insert("c")
    ll2.insert("b")
    ll2.insert("a")
    

    
    print (ll)
    print (ll2)
    zipped_ll=zip_Lists( ll, ll2)
    print(zipped_ll)
    


