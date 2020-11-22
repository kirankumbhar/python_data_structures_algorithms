class Node:
    def __init__(self, data) -> None:
        self.data = data
        self.next = None


def get_input_for_linked_list():
    ch = input("Enter comma separated numbers for linked list: ")
    values = []
    if ch:
        values = [_.strip() for _ in ch.split(",")]
    return values


def create_linked_list(elements: list):
    if not elements:
        return None
    head = None
    current = None
    for element in elements:
        if not head:
            head = Node(element)
            current = head
            continue
        node = Node(element)
        current.next = node
        current = node
    return head


def print_linked_list(head: Node):
    current = head
    if not current:
        print("Linked List is Empty.")
        return
    list_chain = ""
    while current:
        list_chain += current.data + ("=>" if current.next else "")
        current = current.next
    print("======= Linked List ======")
    print("Linked List: " + list_chain)
    print("==========================")


def insert_after(head: Node):
    key = input("Enter key which you want to insert in linked list")
    element = input(
        "Enter the element from linked list after which you want to insert the key"
    )
    if not head:
        return False
    current = head
    while current:
        if current.data == element:
            new_node = Node(key)
            new_node.next = current.next
            current.next = new_node
            return True
        current = current.next
    return False


def insert_before(head: Node):
    key = input("Enter key which you want to insert in linked list")
    element = input(
        "Enter the element from linked list before which you want to insert the key"
    )
    if not head:
        return False, None
    current = head
    prev = current
    while current:
        if current.data == element:
            new_node = Node(key)
            new_node.next = current
            if prev == head:
                return True, new_node
            prev.next = new_node

            return True, None
        prev = current
        current = current.next
    return False, None


def delete(head: Node):
    key = input("Enter element which you want to delete")
    if not head:
        return False, None
    current = head
    prev = None

    while current:
        if current.data == key:
            if not prev:  # the key is the head node
                return True, current.next
            prev.next = current.next
            return True, None
        prev = current
        current = current.next
    return False, None


if __name__ == "__main__":
    elements = get_input_for_linked_list()
    linked_list_head = create_linked_list(elements)
    print_linked_list(linked_list_head)

    print("======= Linked List Insert After operation ======")
    is_inserted = insert_after(linked_list_head)
    if is_inserted:
        print_linked_list(linked_list_head)
    else:
        print("Element not found!")

    print("======= Linked List Insert Before operation ======")
    is_inserted, new_head = insert_before(linked_list_head)
    if is_inserted:
        if new_head:
            linked_list_head = new_head
        print_linked_list(linked_list_head)

    else:
        print("Element not found!")

    print("======= Linked List Delete operation ======")
    is_deleted, new_head = delete(linked_list_head)
    if is_deleted:
        if new_head:
            linked_list_head = new_head
        print_linked_list(linked_list_head)

    else:
        print("Element not found!")
