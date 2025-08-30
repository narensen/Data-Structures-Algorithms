from linked_list import LinkedList

class Queue:

    def __init__(self):
        self.ll = LinkedList()

    def is_empty(self):
        
        return self.ll.head is None
    
    def enqueue(self, value):
        self.ll.append(value)

    def dequeue(self):

        if self.is_empty():
            print("ERROR : Queue is empty")
            return
        
        current = self.ll.head.data
        self.ll.head = self.ll.head.next
        return current
    
    def print_list(self):
        current = self.ll.head

        while current:
            print(current.data)
            current = current.next

if __name__ == "__main__":

    q = Queue()
    q.enqueue(10)
    q.enqueue(20)
    q.print_list()
    print("+----------------------------------------------------+")
    q.dequeue()
    q.print_list()

