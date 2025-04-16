class Singlelinkedlist:
    def __init__(self, value, next = None):
        self.value = value
        self.next = next
    def __str__(self):
        return str(self.value)

Head = Singlelinkedlist(2)
A = Singlelinkedlist(4)
B = Singlelinkedlist(6)
C = Singlelinkedlist(8)

Head.next = A
A.next = B
B.next = C
C.next = None

def display(head):
    curr = head
    arr = []
    while curr:
        arr.append(curr.value)
        curr = curr.next
    return print(f"The linked list is {arr}")

display(Head)

def reverse_linked_list(head):
    curr, prev = head, None
    # should go till curr = None
    while curr:
        next = curr.next
        curr.next = prev
        prev = curr
        curr = next
    return display(prev)

reverse_linked_list(Head)