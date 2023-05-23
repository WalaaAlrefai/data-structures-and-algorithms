def zip_Lists(list1, list2):
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
        if not current1 and current2:
         last_current1.next = current2


    return list1




