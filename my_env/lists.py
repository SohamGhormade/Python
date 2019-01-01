xs = [3, 1, 2]
print(xs, xs[2]) # prints [3, 1, 2 ] 2
print(xs[-1])    # prints 2 Remmember Use [-1] to get the last element.COOL Stuff.
xs[2] = 'foo'
print(xs)        # prints [3,1,'foo']
xs.append('bar')
print(xs)
x = xs.pop() # bar
print(x, xs)

# slicing
nums = list(range(5))
print(nums)       # [0, 1, 2, 3, 4]
print(nums[2:4])  # [2, 3] ,excludes 4.
print(nums[2:])   # [2, 3, 4]
print(nums[:2])   # [0, 1, 2]
print(nums[:])
print(nums[:-1])  # -1 refers to the last index.This excludes the last element.
nums[2:4] =[8,9]
print(nums)
