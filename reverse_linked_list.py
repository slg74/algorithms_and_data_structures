
class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node

    def reverse_list(self):
        prev_node = None
        current_node = self.head
        while current_node is not None:
            next_node = current_node.next
            current_node.next = prev_node
            prev_node = current_node
            current_node = next_node
        self.head = prev_node

    def print_list(self):
        current_node = self.head
        while current_node:
            print(current_node.data)
            current_node = current_node.next

# Create a new linked list
linked_list = LinkedList()

# Append some nodes
linked_list.append(1)
linked_list.append(2)
linked_list.append(3)
linked_list.append(4)

print("Original List:")
linked_list.print_list()  # Output: 1 2 3 4

# Reverse the list
linked_list.reverse_list()

print("Reversed List:")
linked_list.print_list()  # Output: 4 3 2 1


