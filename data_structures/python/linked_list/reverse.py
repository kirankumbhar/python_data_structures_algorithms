from singly_linked_list import (
    Node,
    get_input_for_linked_list,
    create_linked_list,
    print_linked_list,
)


def reverse_linked_list(head: Node):
    prev = None
    current = head
    next_node = None

    while current:
        next_node = current.next
        current.next = prev
        prev = current
        current = next_node
    return prev  # prev becomes heaed at the end


if __name__ == "__main__":
    elements = get_input_for_linked_list()
    linked_list_head = create_linked_list(elements)
    print_linked_list(linked_list_head)
    print("======= Reversed Linked List =======")
    new_head = reverse_linked_list(linked_list_head)
    print_linked_list(new_head)