#selection sort
# searches for a minimum index in each region of the array

# TC: O(n^2)
# Space complexity: O(n)

C = [-5 , 3, 2, 1, -3, -3, 7, 2, 2]

def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_index = 1
        for j in range(i+1, n):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]

selection_sort(C)
print(C)
