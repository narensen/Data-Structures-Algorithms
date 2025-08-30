from linked_list import LinkedList

class Stack:

    def __init__(self):
        self.ll = LinkedList()

    def push(self, value):
        self.ll.prepend(value)

    def pop(self):

        current = self.ll.head
        self.ll.head = self.ll.head.next
        value = current.data

        return value
    
    def print_stack(self):

        current = self.ll.head

        while current:
            print(current.data)
            current = current.next

        return

if __name__ == "__main__":

    s = Stack()

    s.push(2)
    s.push(5)
    s.pop()
    s.print_stack()
    



