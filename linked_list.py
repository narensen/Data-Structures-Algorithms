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

    def delete(self, value):
        if self.head == None:
            return "List empty my boi"
        
        if self.head.data == Node(value):
            self.head = self.head.next
        
        previous_node = self.head
        current_node = self.head.next
        while current_node is not None and current_node.data != value:
            previous_node = current_node
            current_node = current_node.next

        if current_node is None:
            return
        
        previous_node.next = current_node.next
        

if __name__ == "__main__":

    ll = LinkedList()
    ll.append(1)
    ll.append(2)
    ll.prepend(4)
    ll.print_list()
        
