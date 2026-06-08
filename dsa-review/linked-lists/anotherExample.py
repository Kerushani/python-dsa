#singly linked list

class SinglenNode:
    def __init__(self, value, next = None):
        self.value = value
        self.next = next

    def __str__(self):
        return str(self.value)

Head = SinglenNode(1)
A = SinglenNode(3)
B = SinglenNode(4)
C = SinglenNode(7)

Head.next = A
A.next = B
B.next = C

print(Head)

#traverses the list by making a pointer curr and the curr points 
# at each item
curr = Head
while curr:
    print(f"Traverses the list {curr}")
    curr = curr.next

#O(n) display linked list
def display(head):
    curr = head
    elements = []
    while curr:
        elements.append(str(curr.value))
        curr = curr.next
    return elements

print(f"Displays what's in the linked list: {display(Head)}")

#search for an element
def search(head, target):
    curr = head
    # this works because when curr = None aka at the end of the list
    # while loop will be false
    while curr: 
        if curr.value == target:
            return f"{target} IS in the LL"
        curr = curr.next
    return f"{target} IS NOT in the LL"

print(f"Is 2 in the LL? -> {search(Head, 2)} \n Is 7 in the list -> {search(Head, 7)}")