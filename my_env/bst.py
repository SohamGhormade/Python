#write out test code 15 mins


class BST(object):
 "Implement a Binary Search Tree in Python."

 def __init__(self):
  self.root = None
  self.n = 0

 def insert(self, root, val):
  temp = root
  if temp == None:
   temp = TreeNode(val)
   self.n += 1
   return
  if val < temp.val:
   self.insert(temp.left, val)
  else:
   self.insert(temp.right, val)

  return

 def search(self, val, x, parent):
   temp = self.root
   if temp == None:
    return False

   while temp != None:
    if temp.val == val:
     x = temp
     return True

    parent = temp

    if val < temp.val:
     temp = temp.left
    else:
     temp = temp.right

   return False

 def delete(self, val):
   parent = x = None
   found = self.search(val, x, parent)
   if not found:
    return
 # 2 children
   if x.left != None and x.right != None:
    xsucc = x.right
    parent = x

# find leftmost sucessor
   while xsucc.left != None:
    parent = xsucc
    xsucc = xsucc.left

  # set x as xsucc and delete x

   x.val = xsucc.val
   x = xsucc  # treat as one child case

   # no children
   if x.left == None and x.right == None:
    if parent.left == x:
     parent.left = None
    else:
     parent.right = None

   # left child
   if x.left != None and x.right == None:
    if parent.left == x:
     parent.left = x.left
    else:
     parent.right = x.left

   # right child
   if x.left == None and x.right != None:
    if parent.left == x:
     parent.left = x.right
    else:
     parent.right = x.right

   self.n -= 1

 def pre(self, root):
  print("Pre order")
  if root != None:
   print(root.data)
   self.pre(root.left)
   self.pre(root.right)
  else:
   return

 def post(self, root):
  print("Post order")
  if root != None:

   self.post(root.left)
   self.post(root.right)
   print(root.data)
  else:
   return

 def inorder(self, root):
  print("In order")
  if root != None:

   self.inorder(root.left)
   print(root.data)
   self.inorder(root.right)

  else:
   return


class TreeNode(object):
 def __init__(self, val):
  self.val = val
  self.left = None
  self.right = None
#write out test code 15 mins


bst = BST()
assert bst.n == 0

bst.insert(bst.root, 18)
assert bst.n == 1

bst.insert(bst.root, 10)
assert bst.n == 2

bst.insert(bst.root, 5)
assert bst.n == 3

bst.insert(bst.root, 32)
assert bst.n == 4

bst.insert(bst.root, 24)
assert bst.n == 5

bst.insert(bst.root, 25)
assert bst.n == 6

bst.insert(bst.root, 35)
assert bst.n == 7

bst.insert(bst.root, 33)
assert bst.n == 8

bst.inorder(bst.root)
bst.pre(bst.root)
bst.post(bst.root)

bst.delete(4)
assert bst.n == 7
bst.pre(bst.root)

bst.delete(32)
assert bst.n == 6
bst.pre(bst.root)