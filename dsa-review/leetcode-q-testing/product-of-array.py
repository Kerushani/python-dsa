# problem 238

nums = [1, 2, 3, 4]

def productExceptSelf(arr):
    result = [1] * len(arr)
    prefix = 1
    for i in range(len(arr)):
        result[i] = prefix
        prefix *= nums[i]
    postfix = 1
    for i in range(len(arr) - 1, -1, -1):
        result[i] *= postfix
        postfix *= nums[i]
        
    return result

print(productExceptSelf(nums))