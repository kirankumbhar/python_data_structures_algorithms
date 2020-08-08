
import linked_list as li


def swap_nodes(ll, a, b):
    node_a = None
    node_b = None
    prev_node_a = None
    prev_node_b = None

    # iterate over linked list and find out whether a and b exist in linked list, 
    # if exist store node address in noda_a and node_b resp.
    node = ll.head
    prev = None
    while node:
        if node.data == a:
            node_a = node
            prev_node_a = prev
        if node.data == b:
            node_b = node
            prev_node_b = prev
        prev = node
        node = node.next

    if not node_a or not node_b:
        return False

    if prev_node_b == node_a:
        '''
        nodes are adjacent in this case as follows
            1      ->     2    ->  3  ->  4  ->  5
        prev_node_a    node_a   node_b 
                    prev_node_b
        '''
        temp = None
        temp = node_b.next
        node_b.next = node_a
        node_a.next = temp
        if prev_node_a:
            prev_node_a.next = node_b
        else:
            #here one of the node is first node in Linked List
            ll.head = node_b
        return True
    
    if prev_node_a == node_b:
        '''
        nodes are adjacent in this case as follows 
        (This handles the case if someone entered 
        swapped nodes in reverse direction that is 2,1 instead of 1,2)
            1      ->     2    ->  3  ->  4  ->  5
        prev_node_b    node_b   node_a 
                    prev_node_a
        '''
        temp = None
        temp = node_a.next
        node_a.next = node_b
        node_b.next = temp
        if prev_node_b:
            prev_node_b.next = node_a
        else:
            #here one of the node is first node in Linked List
            ll.head = node_a
        return True
    
    '''
    if nodes are not adjacent

    '''
    if prev_node_a:
        prev_node_a.next = node_b
    else:
        ll.head = node_b
    temp = node_b.next
    node_b.next = node_a.next
    node_a.next = temp
    if prev_node_b:
        prev_node_b.next = node_a
    else:
        ll.head = node_a
    
    return True




if __name__ == "__main__":
    ll = li.LinkedList()
    values = ll.get_input_for_linked_list()
    ll.create(values)
    ll.print_linked_list()
    ch = input('Enter values to be swapped with comma separated')
    a, b = [_.strip() for _ in ch.split(',')]

    swap_nodes(ll, a, b)
    ll.print_linked_list()

