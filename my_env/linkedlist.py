# Jai Shree Ram
# Implement LinkedList in Python.
# works fine--tests at the end of the class definition.
# No main() necessary
class LinkedList(object):
# declare static varibles here
# __init__ method is the constructor
  def __init__(self):
        self.first = None
        self.last = None
        self.n = 0

  def size(self):
     return self.n

  def isEmpty(self):
      return self.n == 0

  #insert element at beginning of LinkedList
  def insertAtBeg(self, i):# pass "self" which is the instance
   if self.first == None:
    self.last = self.first = Node(i, None)

   else:
    oldF = self.first
    self.first = Node(i, oldF)

   self.n+=1
  # insert element at the end of LinkedList
  def insertAtEnd(self, i):
   if self.first == None:
     self.last = self.first = Node(i, None)
   else:
     oldL = self.last
     self.last = Node(i, None)
     oldL.next = self.last
   self.n+=1
  # remove at beginning
  def removeAtBeg(self):
   item = None
   if self.first == None:
    # throw exception because no elements to delete
    raise Exception("No elements to delete")
   else:
    item = self.first.val
    self.first = self.first.next

   self.n-=1
   return item
  def removeAtEnd(self):
   if self.first == None:
    raise Exception("No elements to delete")

   temp = self.first
   temp.next != self.last.next
   temp = temp.next

   item = self.last.val
   temp.next = None

   self.n-=1
   return item
# Node
class Node(object):
 def __init__(self, val, next):
  self.val = val
  self.next = next


linkedList = LinkedList()
assert linkedList.size() == 0
assert linkedList.isEmpty(), "LinkedList should be empty"
linkedList.insertAtBeg(3)
assert linkedList.size() == 1
linkedList.insertAtBeg(1)
assert linkedList.size() == 2
linkedList.insertAtBeg(5)
assert linkedList.size() == 3
linkedList.insertAtBeg(6)
assert linkedList.size() == 4

assert linkedList.removeAtBeg()==6 ,"Removed wrong element"
assert linkedList.size() == 3

assert linkedList.removeAtEnd()==3 ,"Removed wrong element"
assert linkedList.size() == 2

assert linkedList.removeAtBeg()==5 ,"Removed wrong element"
assert linkedList.size() == 1

linkedList.insertAtEnd(7)
assert linkedList.size() == 2





