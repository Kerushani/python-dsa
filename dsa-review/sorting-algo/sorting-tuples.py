# sort array of tuples

I = [(-5, 3), (2, 1), (-3,-3), (7,2), (2,2)]

sorts_I = sorted(I, key = lambda t: -t[1])

print(sorts_I)