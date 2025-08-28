class Node:

    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:

    def __init__(self):
        self.head = None

    def print_list(self):
        current = self.head
        while current:
            print(current.data)
            current = current.next

    def append(self, data):
        new_node = Node(data)

        if self.head == None:
            self.head = new_node
            return
        
        current_node = self.head
        while current_node.next:
           current_node = current_node.next

        current_node.next = new_node

        return
    
    def prepend(self, data):
        new_node = Node(data)
        
        new_node.next = self.head
        self.head = new_node

if __name__ == "__main__":

    ll = LinkedList()
    ll.append(1)
    ll.append(2)
    ll.prepend(4)
    ll.print_list()
        
