#  Build Min Heap (Heapify)
# Time: O(n), Space: O(1)

A = [-4, 3, 1, 0, 2, 5, 10, 8, 12, 9]

import heapq
#heapq supports a minimum heap
heapq.heapify(A)

A

# Heap Push (insert element)
# Time: O(log n)

heapq.heappush(A, 4)

# print(A)

#Heap pop (Extract min)
# Time: O(logn)
heapq.heappop(A)

# print(A)

#Heap Sort
#Time complexity: O(nlogn), Space: O(n)
#O(1) is possible via swapping, but this is complex

def heapsort(arr):
    heapq.heapify(arr)
    n = len(arr)
    new_list = [0]*n

    for i in range(n):
        minn= heapq.heappop(arr)
        new_list[i] = minn

    return new_list

heapsort([1, 3, 5, 7, 9, 2, 4, 6, 8, 0])

# Heap Push Pop: Time: O(log n)

heapq.heappushpop(A, 99)
# print(A)

#can make max heap with heapq

B = [-4, 3, 1, 0, 2, 5, 10, 8, 12, 9]
n = len(B)

for i in range(n):
    B[i] = -B[i]

heapq.heapify(B)

print(B)

# prints largest number from the array
largest = -heapq.heappop(B)

print(largest)

# Peak at Min: Time -> O(1)
A[0] 
# min will be whatever's at the root 

#Build heap from scratch
#Time: O(nlogn) -> slower time complexity than calling heapify [O(n)]
C = [-5, 4, 2, 1, 7, 0, 3]
heap = []

for x in C:
    heapq.heappush(heap, x)
    print(heap, len(heap))

#Putting tuples of items on the heap
D = [5, 4, 3, 5, 4, 3, 5, 5, 4]

from collections import Counter

heap2=[]
counter = Counter(D)
print(counter)

for k, v in counter.items():
    heapq.heappush(heap2, (v, k))

print(heap)