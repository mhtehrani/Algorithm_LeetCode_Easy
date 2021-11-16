"""
Is it a Balanced Binary Tree
============================

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

def isBalanced(root):
    def traverse(root, length):
        if not root:
            return True, 0
        elif root.left == None and root.right == None:
            return True, 1
        #end
        
        len_left = 0
        status_left = True
        if root.left != None:
            status_left, len_left = traverse(root.left, 0)
        #end
    
        len_right = 0
        status_right = True
        if root.right != None:
            status_right, len_right = traverse(root.right, 0)
        #end
        
        if not status_left or not status_right:
            return False, 1+max(len_left, len_right)
        elif abs(len_left - len_right) > 1:
            return False, 1+max(len_left, len_right)
        else:
            return True, 1+max(len_left, len_right)
        #end
    #end
    
    length = 1
    check, length = traverse(root, length)
    
    return check
#end

root = TreeNode()
root.val = 3
root.left = TreeNode()
root.left.val = 9
root.right = TreeNode()
root.right.val = 20
root.right.left = TreeNode()
root.right.left.val = 15
root.right.right = TreeNode()
root.right.right.val = 7
root.right.right.right = TreeNode()
root.right.right.right.val = 70

print(isBalanced(root))