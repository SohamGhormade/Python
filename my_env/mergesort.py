def mergesort(a):
 helper = [None] * (len(a)- 1)
 mergesort1(a, helper, 0, len(a) -1)

def mergesort1(a, helper, lo, hi):# Remember no function overloading in Python?
  mid = (lo + hi)/2
  if lo < hi:
   # split into two arrays and then sort
   mergesort1(a, helper, lo, mid)
   mergesort1(a, helper, mid + 1, hi)
   # merge
   merge(a, helper, lo, mid, hi)


def merge(a, helper, lo, mid, hi):
 # copy a into helper
 for i in range( len(a) -1) :
  helper[i] = a[i]

 current = lo
 helperLeft = lo
 helperRight = mid + 1

 # merge
 while helperLeft <= mid and helperRight <= hi:
  if helper[helperLeft] <= helper[helperRight]:
   a[current] = helper[helperLeft]
   helperLeft+=1
  else:
   a[current] = helper[helperRight]
   helperRight+=1

  current+=1

 # copy over remaining elements

 remaining = mid - helperLeft

 for i in range(remaining):
  a[current + i] = helper[helperLeft + i]


inputArray = [5, 1, 4, 3, 8, 11, 2, 6]
mergesort(inputArray)
assert inputArray == [1, 2, 3, 4, 6, 8, 11]

