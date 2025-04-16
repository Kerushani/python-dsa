nums = [1,1,1,2,2,3]
k = 2

dictionary = {}
arr = []

for num in nums:
    if num in dictionary:
        dictionary[num] += 1
    else:
        dictionary[num] = 1

print(dictionary)

for element in dictionary:
    if dictionary[element] >= k:
        arr.append(element)

print(arr)

A = [1, 2, 3]
print(A)

A.append(5)
A.append(9)
print(A)

A.pop()
print(A)

A.insert(2, 5)
print(A)

A[0] = 7
print(A)

if 9 in A:
    print("True")

s = "hello"

b = s + " z"

print(f"The length of b is {len(b)}")

if "e" in s:
    print(f"Yes e is in the string")