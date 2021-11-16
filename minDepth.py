"""
Minimum Binary Tree
===================

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

def minDepth(root):
    def traverse(root):
        len_left = 0
        if root.left != None:
            len_left = traverse(root.left)
        #end
        
        len_right = 0
        if root.right != None:
            len_right = traverse(root.right)
        #end
        
        if len_left != 0 and len_right != 0:
            return 1+min(len_left, len_right)
        else:
            return 1+max(len_left, len_right)
        #end
    #end
    
    if not root:
        return 0
    else:
        return traverse(root)
    #end
#end

root = TreeNode()
root.val = 3
root.left = TreeNode()
root.left.val = 9
root.left.left = TreeNode()
root.left.left.val = 11

root.right = TreeNode()
root.right.val = 20
root.right.left = TreeNode()
root.right.left.val = 15
root.right.right = TreeNode()
root.right.right.val = 7
root.right.right.right = TreeNode()
root.right.right.right.val = 70

print(minDepth(root))