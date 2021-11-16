"""
Is the Binary Trees Symmetric
=============================

@author: mhtehrani
November 03, 2021
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

def isSymmetric(root):
    if root.left == None and root.right == None:
        return True
    #end
    
    p = root.left
    q = root.right
    
    def traverse(p,q):
        check = True
        if p.left == None and p.right == None:
            if q.left == None and q.right == None:
                if p.val != q.val:
                    return False
                else:
                    return True
                #end
            else:
                return False
            #end
        elif q.left == None and q.right == None:
            return False
        #end
        
        if p.left != None:
            if q.right != None:
                check = traverse(p.left,q.right)
                if not check:
                    return check
                #end
            else:
                return False
            #end
        else:
            if q.right != None:
                return False
            #end
        #end
        
        if p.right != None:
            if q.left != None:
                check = traverse(p.right,q.left)
                if not check:
                    return check
                #end
            else:
                return False
            #end
        else:
            if q.left != None:
                return False
            #end
        #end
            
        if p.val != q.val:
            return False
        #end
        
        return check
    #end
    
    if p:
        if q:
            return traverse(p,q)
        else:
            return False
        #end
    elif q:
        return False
    else:
        return True
    #end
#end

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

print(isSymmetric(H3))



