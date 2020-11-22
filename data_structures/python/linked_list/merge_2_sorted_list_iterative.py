from singly_linked_list import (
    Node,
    get_input_for_linked_list,
    create_linked_list,
    print_linked_list,
)


def merge_2_sorted_list(head1: Node, head2: Node):
    current1 = head1
    current2 = head2
    head = None
    prev = None
    while current1 or current2:
        if current1 and current2:
            if current1.data < current2.data:
                if not head:
                    head = current1
                else:
                    prev.next = current1
                prev = current1
                current1 = current1.next
            else:
                if not head:
                    head = current2
                else:
                    prev.next = current2
                prev = current2
                current2 = current2.next
        elif current1:
            if not head:
                head = current1
            else:
                prev.next = current1
            prev = current1
            current1 = current1.next
        elif current2:
            if not head:
                head = current2
            else:
                prev.next = current2
            prev = current2
            current2 = current2.next
    return head


if __name__ == "__main__":
    print("Input for Linked List 1")
    values = get_input_for_linked_list()
    linked_list_1 = create_linked_list(values)
    print("Input for Linked List 2")
    values = get_input_for_linked_list()
    linked_list_2 = create_linked_list(values)
    new_head = merge_2_sorted_list(linked_list_1, linked_list_2)
    print("Merged Linked List")
    print_linked_list(new_head)
