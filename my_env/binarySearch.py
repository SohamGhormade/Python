def binarySearch(nums, lo, hi, x):
 mid = int((lo + hi)/2)# cast to int
 while lo < hi:
  if nums[mid] == x:
   return mid

  if nums[mid] < x:
   return binarySearch(nums,mid+ 1, hi, x)

  else:
   return binarySearch(nums, lo, mid, x)

a = [3,4,5,6,88,90,7890]
assert binarySearch(a,0,len(a) -1 ,88) == 4, "wrong index for 88"
#assert binarySearch(a,0,len(a) -1 ,7) == , "element not found"
assert binarySearch(a,0,len(a) -1 ,3) == 0,'wrong index for 3 '