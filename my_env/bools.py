t = True
f = False
print(type(t)) # prints "<class 'bool'>"
print(t and f) # LOGICAL AND prints False
print(t or f) # LOGICAL OR prints True
print(not t) #LOGICAL XOR prints False
print(t !=f )# LOGICAL XOR prints True
hello = 'hello' # strings okay with single quotes
world = "world"
print(hello)
print(world)
print(len(hello)) # Use len() to get string length
hw = hello + world #string concatenation
print(hw)
hw12 = '%s, %s, %d' %(hello, world, 12)
print(hw12)

