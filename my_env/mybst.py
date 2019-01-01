# Jai Shree Ram
# implement a BST in Python
# Works fine.

class BST(object):
    'Binary Search Tree'
    def __init__(self):
     self.root = None
     self.n = 0

    def insert(self, val):
        self.root = self.__insert(val,self.root)

# Remember,Python does not support "pass by reference"
# so you need to return the value as a single value,list ,dictionary or a tuple
    def __insert(self, val, root):
     if root == None:
      self.n += 1
      return Node(val)

     if val > root.val :
      root.right = self.__insert(val, root.right)
     else:
      root.left = self.__insert(val, root.left)
     return root

    def size(self):
     return self.n

    def search(self, val):
     x = parent = None
     if self.root is None:
      return (False, x, parent)

     temp = self.root
     while temp is not None:

      if temp.val == val :
       x = temp
       print('Found',x.val,'with parent ',parent.val)
       return (True, x, parent)

      parent = temp
      if val > temp.val:
       temp = temp.right
      else:
       temp = temp.left

     return (False, x, parent)

    def delete(self, val):
      self.__delete(val,self.root)

    def __delete(self, val, root):

     (found, x, parent) = self.search(val)

     if not found :
      return
     # two children
     if x.left is not  None and x.right is not  None:
      xsucc = x.right
      parent = x
      while xsucc.left is not  None:
       parent = xsucc
       xsucc = xsucc.left

      x.val = xsucc.val
      x = xsucc

     # left child
     if x.left is not None and x.right ==  None:
      if parent.left == x:
        parent.left = x.left
      else:
        parent.right = x.left

     # right child
     if x.left ==  None and x.right  is not  None:
      if parent.left == x:
        parent.left = x.right
      else:
        parent.right = x.right

     # no children
     if x.left == None and x.right ==  None:
      if parent.left == x:
        parent.left = None
      else:
        parent.right = None

     self.n-=1

    def preorder(self):
     print('pre order')
     self.__preorder(self.root)
     print()

    def __preorder(self, root):
     if root is not None:
      print(root.val, end =' ')# prevent on same line
      self.__preorder(root.left)
      self.__preorder(root.right)
     else:
      return

    def postorder(self):
     print('post order')
     self.__postorder(self.root)
     print()

    # Remember to use triple quotes for multi-line comments in Python
    def __postorder(self, root):
     '''
     private method is created by name mangling.
     You can mangle method names by prepending two _ to its name
     '''
     if root is not None:
      self.__postorder(root.left)
      self.__postorder(root.right)
      print(root.val, end =' ')
     else:
       return

    def inorder(self):
     print('in order')
     self.__inorder(self.root)
     print()

    def __inorder(self, root):
      '''
      private method is created by name mangling.
      You can mangle method names by prepending two _ to its name
      '''
      if root is not None:
       self.__inorder(root.left)
       print(root.val, end = ' ')
       self.__inorder(root.right)

      else:
       return


class Node(object):
 "Node for BST"
 def __init__(self, val):
  self.val = val
  self.left = None
  self.right = None

bst = BST()

bst.insert(5)

assert bst.size() == 1
bst.inorder()

bst.insert(1)
assert bst.size() == 2
bst.inorder()

bst.insert(18)
assert bst.size() == 3
bst.inorder()

bst.insert(0)
assert bst.size() == 4
bst.inorder()

bst.insert(4)
assert bst.size() == 5
bst.inorder()

bst.insert(21)
assert bst.size() == 6
bst.inorder()

bst.insert(19)
assert bst.size() == 7

bst.preorder()

bst.inorder()

bst.postorder()
bst.delete(4)
assert bst.size() == 6
bst.inorder()

bst.delete(18)
assert bst.size() == 5
bst.inorder()

