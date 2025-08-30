class Node:

    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def print_list(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")

    def append(self, data): # O(1)
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
            return
        
        # No loop needed. We use the tail pointer.
        self.tail.next = new_node
        self.tail = new_node

    def prepend(self, data): # O(1)
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
            return

        new_node.next = self.head
        self.head = new_node

    def delete(self, value): # O(n)
        if self.head is None:
            return

        # If the head is the node to delete
        if self.head.data == value:
            # If it's also the only node
            if self.head == self.tail:
                self.head = None
                self.tail = None
            else:
                self.head = self.head.next
            return

        # Traverse to find the node
        previous = self.head
        current = self.head.next
        while current is not None and current.data != value:
            previous = current
            current = current.next

        # If node was found
        if current is not None:
            # If it's the tail node
            if current == self.tail:
                self.tail = previous
            
            previous.next = current.next
        

if __name__ == "__main__":

    ll = LinkedList()
    ll.append(1)
    ll.append(2)
    ll.delete(2)
    ll.prepend(4)
    ll.print_list()
        
