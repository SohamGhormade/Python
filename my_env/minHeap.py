
class MinHeap:
  "Implements a Min binary heap in Python"
  def __init__(self):
   self.a = [None]*10000# fixed size array
   self.a[0] = -1 # sentinel value
   self.n = 0



  def swim(self, k):
   "bottom up re-heapify"
   while k > 1:
    self.a[k] < self.a[k/2]
   self.swap(k, k/2)
   k = k/2

  def sink(self, k):
   "top down re-heapify"
   child = 0

   while 2*k < self.n:
    child = 2 *k
    if self.a[child] > self.a[child + 1]:
     self.swap(child, child + 1)
    k = child

  def swap(self, x, y):
      temp = self.a[x]
      self.a[x] = self.a[y]
      self.a[y] = temp

  def delMin(self):
   "deletes the smallest element"
   minM = self.a[1]
   self.swap(1, self.n)
   self.sink(1)k

   self.a[self.n] = None
   self.n -= 1
   return minM

  def size(self):
   return self.n

  def isEmpty(self):
   return self.n == 0
  def peek(self):
   return self.a[1]

  def insert(self, value):
   "adds an element to the heap "
   self.n +=1
   self.a[self.n] = value
   self.swim(self.n)


heap = MinHeap()
assert heap.isEmpty()

heap.insert(200)
assert not heap.isEmpty()
assert heap.peek() == 200
assert heap.size() == 1

heap.insert(30)
assert heap.peek() == 30
assert heap.size() == 2

heap.insert(45)

heap.insert(5)
assert heap.peek() == 5
assert heap.size() == 4

heap.insert(3)
assert heap.peek() == 3
assert heap.size() == 5

heap.insert(4)
heap.insert(330)
heap.insert(454)

assert heap.peek() == 3
assert heap.size() == 8

assert heap.delMin() == 3
assert heap.peek() == 4
assert heap.size() == 7

assert heap.delMin() == 4
assert heap.size() == 6

heap.insert(33)
assert heap.delMin() == 5
assert heap.size() == 5
