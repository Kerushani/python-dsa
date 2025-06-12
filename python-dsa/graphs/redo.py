""""
dfs uses a stack -> pop() FIFO -> pop node and add connections to the stack

bfs uses a queue -> popleft() LIFO 

good at describing the relationship between things

hashmap can be used to represent an adjacency list
i.e.
{
    a: [b, c],
    b: [d].
    c: [e],
    d: [],
    e: [b],
    f: [d]
}

dfs -> would go down a path in the deep direction ; exploring one direction as far as possible
bfs -> explore immediate neighbours of the node

"""
# using a stack -> LIFO
import collections


def dfs(graph, source):
    stack = [ source ]
    while (len(stack) > 0):
        current = stack.pop()
        # print(current)
        for neighbour in graph[current]:
            stack.append(neighbour)


def dfs_Recursive(graph, source):
    # print(source)
    for neighbour in graph[source]:
        dfs(graph, neighbour)

# adjency matrix
graph  ={
    "a": ["b", "c"],
    "b": ["d"],
    "c": ["e"],
    "d": ["f"],
    "e": [],
    "f":[]
}

dfs(graph, "a")
dfs_Recursive(graph, "a")

# bfs

def bfs(graph, source):
    queue = collections.deque(source)
    while(len(queue) > 0):
        current = queue.popleft()
        print(current)
        for neighbour in graph[current]:
            queue.append(neighbour)

bfs(graph, "a")

def hasPath(graph, src, dst):
    if (src == dst): return True

    for neighbour in graph[src]:
        if(hasPath(graph,neighbour,dst) == True): return True
    return False

def hasPath(graph, src, dst):
    queue = [src]
    while (len(queue) > 0):
        current = queue.pop()
        if (current == dst): return True
        # collects all the neighbours from the src
        for neighbour in graph[current]:
            queue.append(neighbour)
    return False

print(hasPath(graph, "a", "e"))