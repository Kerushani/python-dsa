class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insert_front(self, value):
        print("Inserting", value)
        new_node = Node(value)
        new_node.next = self.head
        self.head = new_node
    
    def get_head_value(self):
        if self.head is None:
            return -1
        else:
            return self.head.value

list = LinkedList()
list.insert_front(3)
print("The values of the head is:", list.get_head_value())

list.insert_front(4)
print("The values of the head is:", list.get_head_value())

list.insert_front(6)
print("The values of the head is:", list.get_head_value())

