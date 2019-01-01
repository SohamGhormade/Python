# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode

        """
        if len(nums) == 0 :
            return None

        if len(nums) == 1:
            return TreeNode(nums[0])

        # find root
        lo = 0
        hi = len(nums)
        mid = int((lo + hi)/2)

        i = mid - 1
        j = mid + 1
        # insert the root
        root = TreeNode(nums[mid])

        while i >=0 and j < len(nums):
            root = self.insert(nums[i], root)
            print(nums[i])
            print(nums[j])
            root = self.insert(nums[j], root)
            i-=1
            j+=1

        return root


    def insert(self, value, root):
        if root == None:
            root = TreeNode(value)

        elif value > root.val :
            self.insert(value, root.right)
        else:
            self.insert(value, root.left)
        return root

