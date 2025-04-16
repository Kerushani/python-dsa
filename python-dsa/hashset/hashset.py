s = set()
print(s)

s.add(1)
s.add(2)
s.add(3)

print(s)

# Look up if iten in set - O(1)
if 1 not in s: 
    print(True)

s.remove(3)

print(s)

string = "aaaaabbbbbccccceeeee"
sett = set(string)
print(sett)

#Hashmaps - Dictionaries

d = {"greg": 1, "steve":2, "rob":3}
print(d)

#Add key:val in dictionary: O(1)
d["arsh"] = 4

print(d)

#Loop over something

if "greg" in d:
    print("true")

for key, value in d.items():
    print(f"key: {key} value: {value}")