class DoubleLinkedList:
    def __init__(self, value, next=None, prev=None):
        self.value = value
        self.next = next
        self.prev = prev

    def __str__(self):
        return str(self.value)
    
head = tail = DoubleLinkedList(1)
print(f"The tail is {tail} \nThe heads in {head}")

def display(head):
    curr = head
    elements = []
    while curr:
        elements.append(str(curr.value))
        curr = curr.next
    print("<->".join(elements))

#Insert at beginning
def insert_at_beginning(head, tail, value):
    new_node = DoubleLinkedList(value, next=head)
    head.prev = new_node
    return new_node, tail

head, tail = insert_at_beginning(head, tail, 3)
head, tail = insert_at_beginning(head, tail, 4)


def insert_at_end(head, tail, val):
    new_node = DoubleLinkedList(val, prev=tail)
    tail.next = new_node
    return head, new_node

head, tail = insert_at_end(head, tail, 7)
display(head)