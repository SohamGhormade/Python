# Python Sets:- *unordered* collection of distinct elements
# like a HashSet in C#.

animals = {'cat', 'dog'}
print('cat' in animals)# True
print('fish' in animals) # False
animals.add('fish')
print('fish' in animals)# True
print(len(animals)) # 3
print(animals.remove('cat'))
print(len(animals)) # 2

for idx, animal in enumerate(animals):
  print('#%d: %s' %(idx + 1, animal))

from math import sqrt
nums = {int(sqrt(x)) for x in range(30)}

print(nums)
# Tuples -- immumtable ordered lists
# - tuple can be used as keys in dictionaries
# can be used as elements of sets
d = {(x, x+1) : x for x in range(10)}
t = (5,6) # creates a tuple
print(type(t))
print(d[t]) # prints 5
print(d[1,2])# prints 1
