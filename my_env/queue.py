# no using statements or import statements for Python.Yay!
# works fine.
class Queue(object):
  " implement a Queue in Python"

  def __init__(self):
    " create an empty queue"
    self.first = None
    self.last = None
    self.n = 0


  def enqueue(self, value):
   "add element to queue"
   if self.first == None:
      self.first = self.last = Node(value, None)

   else:
    oldLast = self.last
    self.last = Node(value, None)
    oldLast.next = self.last

   self.n+=1

  # Syntax :summary comments go 'after' the method signature in python
  def dequeue(self):
    "remove last element from queue"
    item = None
    if self.first == None:
     raise Exception("No elements to delete.The queue is empty")# raise is the keyword instead of throw
     # for throwing exceptions
    else:
      item = self.first.value
      self.first = self.first.next

    self.n -=1
    return item


  def size(self):
    'returns size of the queue'
    return self.n


  def isEmpty(self):
    "Returns true if Queue is empty"
    return self.n == 0

"Can we create struct in Python?"
class Node(object):
 def __init__(self, value, next):
  self.value = value
  self.next = next


#Test code

q = Queue()
assert q.isEmpty(), "Queue should be empty"
q.enqueue('a')
assert 1 == q.size()
q.enqueue('f')
assert 2 == q.size()
assert 'a'== q.dequeue(),""
assert 1 == q.size()
q.enqueue('c')
q.enqueue('d')
assert 3 == q.size()
assert 'f'== q.dequeue(),""


