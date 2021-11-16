"""
Has a Binary Tree a Path SUM Equal to Target
============================================

@author: mhtehrani
November 05, 2021
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

def hasPathSum(root,targetSum):
    if not root:
        return False
    #end
    
    newTargetSum = targetSum-root.val
    if newTargetSum == 0 and root.left == None and root.right == None:
        return True
    #end
        
    left = False
    if root.left != None:
        left = hasPathSum(root.left, newTargetSum)
    #end
    
    if left == True:
        return True
    #end
    
    right = False
    if root.right != None:
        right = hasPathSum(root.right, newTargetSum)
    #end
    
    if left or right:
        return True
    else:
        return False
    #end
#end



root = TreeNode()
root.val = 5
root.left = TreeNode()
root.left.val = 4
root.left.left = TreeNode()
root.left.left.val = 11
root.left.left.left = TreeNode()
root.left.left.left.val = 7
root.left.left.right = TreeNode()
root.left.left.right.val = 2

root.right = TreeNode()
root.right.val = 8
root.right.left = TreeNode()
root.right.left.val = 13
root.right.right = TreeNode()
root.right.right.val = 4
root.right.right.right = TreeNode()
root.right.right.right.val = 1

print(hasPathSum(root,22))