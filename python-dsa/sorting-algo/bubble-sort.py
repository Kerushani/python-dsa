# Bubble Sort
# Time: O(n^2)
#Space: O(1)

A = [-5, 3, 2, 1, -3, -3, 7, 2, 2]

print(A)

def bubble_sort(arr):
    n = len(arr)
    flag = True
    while flag:
        flag = False
        for i in range(1, n):
            # if index before is larger than index after
            #decending is arr[i-1] < arr[i]
            if arr[i-1] > arr[i]:
                flag = True
                arr[i-1],arr[i] = arr[i], arr[i-1]

bubble_sort(A)
print(A)
