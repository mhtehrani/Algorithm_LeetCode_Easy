"""
Convert a Sorted Array to a Balanced Binary Tree
================================================

@author: mhtehrani
November 04, 2021
https://github.com/mhtehrani

"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
    #end
#end

def sortedArrayToBST(nums):
    def traverse(nums):
        if len(nums) == 0:
            return None
        elif len(nums) == 1:
            root = TreeNode()
            root.val = nums[0]
            return root
        #end
        
        n = len(nums)//2
        
        root = TreeNode()
        root.val = nums[n]
        
        root.left = traverse(nums[:n])
        
        root.right = traverse(nums[n+1:])
        
        return root
    #end
    
    if len(nums) == 0:
        return None
    #end
    
    return traverse(nums)
#end

nums = [-10,-3,0,5,9]
print(sortedArrayToBST(nums))