import linked_list as li

def detect_cycle(ll):
    """
    Floyd detect cycle algorithm uses 2 pointer called slow_pointer and fast_pointer
    Using iterative approach slow pointer always points to next node in linked list and
    fast pointer always points to the next of the next node (current  + 2)
    if loop exists fast pointer will meet slow pointer both pointing to same node
    else no loop exists
    """

    slow_p = fast_p = ll.head

    while (slow_p and fast_p and fast_p.next):
        slow_p = slow_p.next
        fast_p = fast_p.next.next

        if(slow_p == fast_p):
            return True
    return False

def create_cycle(ll):
    """
    This function created cycle in given linked list intentionally
    by pointing last node to head
    """

    node = ll.head

    while(node.next):
        node = node.next
    node.next = ll.head
    

if __name__ == "__main__":
    ll = li.LinkedList()
    values = ll.get_input_for_linked_list()
    ll.create(values)
    ll.print_linked_list()
    # Call create_cycle() for detact_cycle() to return true
    # create_cycle(ll)
    if detect_cycle(ll):
        print('Linked List contains loop')
    else:
        print('Linked List does not contain loop')
