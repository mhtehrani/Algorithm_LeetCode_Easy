"""
Binary Tree Inorder Traversal
=============================

@author: mhtehrani
November 02, 2021
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

def inorderTraversal(root):
    def traverse(root,List):
        if root.left == None and root.right == None:
            return List.append(root.val)
        #end
        
        if root.left != None:
            traverse(root.left,List)
        #end
        
        List.append(root.val)
        
        if root.right != None:
            traverse(root.right,List)
        #end
        
        return List
    #end
    
    List = []
    
    if root:
        traverse(root,List)
    #end
    
    return List
#end












root = [1, None, 2, 3]

Head = TreeNode()
Head.val = 1
# Head.left =
Head.right = TreeNode()
Head.right.val = 2
Head.right.left = TreeNode()
Head.right.left.val = 3

Head2 = TreeNode()
Head2.val = 1

Head3 = TreeNode()
Head3.val = 1
Head3.left = TreeNode()
Head3.left.val = 2

Head4 = TreeNode()
Head4.val = 1
Head4.right = TreeNode()
Head4.right.val = 2

print(inorderTraversal(Head))
print(inorderTraversal([]))
print(inorderTraversal(Head2))
print(inorderTraversal(Head3))
print(inorderTraversal(Head4))