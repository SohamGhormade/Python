animals = ['cat','dog', 'monkey']

for animal in animals:
  print(animal)

# use enumerate to get index for list
for idx,animal in enumerate(animals):
  print('%d %s' %(idx + 1, animal))

# list comprehensions
nums = [0,1,2,3,4]
squares = []
for x in nums:
  squares.append(x**2)# exponentiation

print(squares)

even_squares = [x**2 for x in nums if x%2 == 0]# used conditionals in lists
print(even_squares)# print a list in one line


