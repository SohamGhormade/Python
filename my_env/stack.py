

#Node
class Node(object):
  def __init__(self, value, next):
    self.value = value
    self.next = next

# implement a stack in Python
# works fine.
class Stack(object):
  def __init__(self):
    self.top = Node(0, None)
    self.n = 0

  def push(self, value):
    if self.top == None:
      self.top = Node(value, None)

    else:
      oldTop = self.top
      self.top = Node(value, oldTop)

    self.n +=1 # Syntax: python does not support unary operators like ++ and --

  def pop(self):
    item = None
    if self.top == None:
        raise Exception ("No elements remaining to pop!")
    else:
     item = self.top.value
     self.top = self.top.next

    self.n -=1
    return item

  def isEmpty(self):
     return self.n == 0

  def size(self):
     return self.n

# ResizingStack in Python
class ResizingStack(object):
 def __init__(self):
  self.n = 0
  self.a = [None]# Syntax:1 element empty list

 def peek(self):
   "the next item to be popped"
   temp = self.n - 1
   return  self.a[temp]

 def pop(self):
     if self.n < len(self.a)/4:
      self.resize(int(len(self.a)/2))

     self.n -= 1
     item = self.a[self.n]
     print (item, " ")
     return item

 def push(self, i):
   if self.n == len(self.a):
       self.resize(2 *self.n)
   self.a[self.n] = i
   self.n +=1


 def resize(self, size):
 # min = self.n > size  if size else self.n# Syntax: ternary operator
  t =  [None]*size #empty list of size "size"
  for i in range(self.n) :# for loop
   t[i] = self.a[i]

  self.a = t

 def size(self):
   return self.n

 def isEmpty(self):
   return self.n == 0


s = Stack()
assert s.isEmpty() ,"Should be empty because elements added"

s.push(13)
assert s.size() == 1, "Size should be 1 because one element was added"

s.push(23)
assert s.size() == 2, ""

s.push(55)
assert s.size() == 3, ""

assert 55 == s.pop()
assert s.size() == 2, ""

s.push(34)
assert s.size() == 3, ""

assert 34 == s.pop()
assert s.size() == 2, ""

# ResizingStack
s = ResizingStack()
assert s.isEmpty() ,"Should be empty because elements added"

s.push(13)
assert s.size() == 1, "Size should be 1 because one element was added"
print(s.peek())
s.push(23)
assert s.size() == 2, ""
print(s.peek())
s.push(55)
assert s.size() == 3, ""
print(s.peek())
assert 55 == s.pop()
assert s.size() == 2, ""

s.push(34)
assert s.size() == 3, ""

assert 34 == s.pop()
assert s.size() == 2, ""

