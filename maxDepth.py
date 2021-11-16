"""
Maximum Depth of a Tree
=======================

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

def maxDepth(root):
    if not root:
        return 0
    elif root.left == None and root.right == None:
        return 1
    #end
    
    LeftDepth = 0
    if root.left != None:
        LeftDepth = maxDepth(root.left)
    #end
    
    RightDepth = 0
    if root.right != None:
        RightDepth = maxDepth(root.right)
    #end

    return 1 + max(LeftDepth,RightDepth)
#end


H0 = TreeNode()
H0.val = 1

H0.left = TreeNode()
H0.left.val = 2

H0.left.left = TreeNode()
H0.left.left.val = 3

H0.left.right = TreeNode()
H0.left.right.val = 3

H0.left.left.left = TreeNode()
H0.left.left.left.val = 3

H0.left.left.left.right = TreeNode()
H0.left.left.left.right.val = 3

H0.left.right.right = TreeNode()
H0.left.right.right.val = 3

H0.left.right.right.left = TreeNode()
H0.left.right.right.left.val = 3

H0.left.right.right.left.left = TreeNode()
H0.left.right.right.left.left.val = 3

H1 = TreeNode()
H1.val = 1

H1.left = TreeNode()
H1.left.val = 2

H1.right = TreeNode()
H1.right.val = 2

H1.left.right = TreeNode()
H1.left.right.val = 3

H1.right.right = TreeNode()
H1.right.right.val = 3


H2 = TreeNode()
H2.val = 1

H2.left = TreeNode()
H2.left.val = 2

H2.right = TreeNode()
H2.right.val = 2

H2.left.left = TreeNode()
H2.left.left.val = 3

H2.right.right = TreeNode()
H2.right.right.val = 3


H3 = TreeNode()
H3.val = 1

H3.left = TreeNode()
H3.left.val = 2

H3.right = TreeNode()
H3.right.val = 2

H3.left.right = TreeNode()
H3.left.right.val = 3

H3.right.left = TreeNode()
H3.right.left.val = 3

print(maxDepth(H0))
print(maxDepth(H1))
print(maxDepth(H2))
print(maxDepth(H3))
