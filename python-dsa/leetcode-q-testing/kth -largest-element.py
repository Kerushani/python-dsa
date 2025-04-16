#Min-Heap question

import heapq

class KthLargest:
    def __init__(self, k, nums):
        self.k = k
        self.heap = nums
        heapq.heapify(self.heap)
        while len(self.heap) > k:
            heapq.heappop(self.heap)

    def add(self, val):
        heapq.heappush(self.heap, val)
        if len(self.heap) > self.k:
            heapq.heappop(self.heap)
        return self.heap[0]

commands = ["KthLargest", "add", "add", "add", "add", "add"]
arguments = [[3, [4, 5, 8, 2]], [3], [5], [10], [9], [4]]

output = []

kth_largest_obj = None

for cmd, arg in zip(commands, arguments):
    if cmd == "KthLargest":
        k, nums = arg
        kth_largest_obj = KthLargest(k, nums)
        output.append(None)
    elif cmd == "add":
        val = arg[0]
        result = kth_largest_obj.add(val)
        output.append(result)

print("Output:", output)
