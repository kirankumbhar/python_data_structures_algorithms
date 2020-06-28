class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
    
    def create(self, numbers):
        if not numbers:

            return
        self.head = Node(numbers[0])
        current = self.head
        for number in numbers[1:]:
            node = Node(number)
            current.next = node
            current = node

    def reverse(self):
        if not self.head or not self.head.next:
            return
        prev_node = None
        current_node = self.head
        while(current_node):
            next_node = current_node.next
            current_node.next = prev_node 
            prev_node = current_node
            current_node = next_node
        self.head = prev_node
        


    
    def print_linked_list(self):
        current = self.head
        if not current:
            print('Linked List is Empty.')
            return
        list_chain = ''
        while(current):
            list_chain +=  current.data + ('=>' if current.next else '')
            current = current.next
        print('Linked List: ' + list_chain)


if __name__ == "__main__":
    ch = input('Enter comma separated numbers for linked list: ')
    values = []
    if ch:
        values = [_.strip() for _ in ch.split(',')]
    ll = LinkedList()
    ll.create(values)
    ll.print_linked_list()
    ll.reverse()
    ll.print_linked_list()

