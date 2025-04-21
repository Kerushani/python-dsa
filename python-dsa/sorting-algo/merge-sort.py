# "divide and conquer"
# find middle of array 
# split each split array to many smaller array until individual elements
# uses recursion ; use l and r pointers to compare values in each array

# Merge sort
# Time: O(n log n)
# Space: O(n) - Note: can be Log n, but this is harder to write

D = [-5, 3, 2, 1, -3, -3, 7, 2, 2]

#won't have arr of length 0
def merge_sort(arr):
    n = len(arr)

    if n == 1:
        return arr
    
    m = len(arr) // 2
    # take all the elements from the start of the list up to, but not including, index m
    L = arr[:m]
    # take all the elements from the end of the list up to, but not including, index m
    R = arr[m:]

    L = merge_sort(L)
    R = merge_sort(R)
    l, r = 0, 0
    L_len = len(L)
    R_len = len(R)

    sorted_arr = [0] * n
    i = 0

    while l < L_len and r < R_len:
        if L[l] < R[r]:
           sorted_arr[i] = L[l]
           l += 1
        else:
           sorted_arr[i] = R[r]
           r += 1
        i += 1

    while l < L_len:
        sorted_arr[i] = L[l] 
        l += 1
        i += 1
    
    while r < R_len:
        sorted_arr[i] = R[r]
        r += 1
        i += 1

    return sorted_arr

print(merge_sort(D))