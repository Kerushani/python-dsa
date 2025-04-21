# Array of edges (directed) [Start, End]

n = 8

A = [[0,1], [1,2], [0,3],[3,4],[3,6], [3,7], [4,2], [4,5], [5,2]]

print(A)

# Convert Array of Edges -> Adjacency Matrix
M = []
for i in range(n):
    M.append([0]*n)

for u, v in A:
    M[u][v] = 1

    #uncommet if the following line of the graph is undirected
    # M[u][v] = 1

# print(M)

# --------
# Convert Array of Edges -> Adjacency List (hashmap with what each num points to)
from collections import defaultdict

D = defaultdict(list)

for u, v in A:
    D[u].append(v)

    # uncomment for undirected
    D[v].append(u)

# ------
# DFS with recursion - O(V + E) where V is the number of nodes and E is the number of edges
def dfs_recursive(node):
    print(node) 
    for nei_node in D[node]:
        if nei_node not in seen:
            seen.add(nei_node)
            dfs_recursive(nei_node)
source = 0 

seen = set()
seen.add(source)
print(dfs_recursive(source))


# ////
# Iterative DFS with Stack - O(V+E)

source = 0
seen = set()
seen.add(source)
stack = [source]

while stack:
    node = stack.pop()
    print(node)
    for nei_node in D[node]:
        if nei_node not in seen:
            seen.add(nei_node)
            stack.append(nei_node)

# BFS(QUEUE) - O(V + E)
source  = 0
from collections import deque

seen = set()
seen.add(source)
q = deque()
q.append(source)

while q:
    node = q.popleft()
    print(node)
    for nei_node in D[node]:
        if nei_node not in seen:
            seen.add(nei_node)
            q.append(nei_node)
 
#  -----
# using classes to make graphs

class Node:
    def __init__(self, value):
        self.value = value
        self.neighbours = []

    def __str__(self):
        return f"Node({self.value})"
    
    def display(self):
        connections = [node.value for node in self.neighbours]
        return f"{self.value} is connected to: {connections}"
    
    A = Node("A")
    B = Node("B")
    C = Node("C")
    D = Node("D")

    A.neighbours.append(B)
    B.neighbours.append(A)

    C.neighbours.append(D)
    D.neighbours.append(C)