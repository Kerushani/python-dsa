from collections import deque

class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
    
    def __str__(self):
        return str(self.val)
    
A = TreeNode(1)
B = TreeNode(2)
C = TreeNode(3)
D = TreeNode(4)
E = TreeNode(5)
F = TreeNode(10)

A.left = B
A.right = C
B.left = D
B.right = E
C.left = F

def pre_order(node):
    if not node:
        return
    print(node)
    pre_order(node.left)
    pre_order(node.right)

# pre_order(A)

def in_order(node):
    if not node:
        return
    in_order(node.left)
    print(node)
    in_order(node.right)

# in_order(A)

def pre_order_iterative(node):
    stk = [node]
    # if not node:
    #     node
    # post_order(node.left)
    # post_order(node.right)
    # print(node)
    while stk:
        node = stk.pop()
        print(node)
        if node.right: stk.append(node.right)
        if node.left: stk.append(node.left)

# pre_order_iterative(A)

def level_order(node):
    q = deque()
    q.append(node)

    while q: 
        node = q.popleft()
        print(node)
        if node.left: q.append(node.left)
        if node.right: q.append

level_order(A)

def search(node, target):
    if not node:
        return print("False")
    if node.val == target:
        return print("True")
    
    return search(node.left, target) or search(node.right, target)

search(A, 10)