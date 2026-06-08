# binary-search
target = 9
nums = [-1, 0, 3, 5]

def solutions():
    l, r = 0, len(nums)-1
    if target > nums[len(nums)-1]:
        return -1
    while l <= r:
        mid = nums[(l+r)//2]
        print(f"left{l} and right{r}")
        print(f"target{target} and mid{mid}")
        if mid == target:
            return (l+r)//2
        if target < mid:
            r = (l+r)//2 - 1
        if target > mid:
            l = (l+r)//2 - 1
    return -1

print(solutions())