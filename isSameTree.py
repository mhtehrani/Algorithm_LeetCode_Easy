"""
Is Two Binary Trees the Same
============================

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

def isSameTree(p, q):
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
            if q.left != None:
                check = traverse(p.left,q.left)
                if not check:
                    return check
                #end
            else:
                return False
            #end
        elif q.left != None:
            return False
        #end
            
        if p.val != q.val:
            return False
        #end
        
        if p.right != None:
            if q.right != None:
                check = traverse(p.right,q.right)
                if not check:
                    return check
                #end
            else:
                return False
            #end
        elif q.right != None:
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

Head = TreeNode()
Head.val = 1
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

Head5 = TreeNode()

H6 = TreeNode()
H6.val = 3
H6.left = TreeNode()
H6.left.val = 9
H6.right = TreeNode()
H6.right.val = 20
H6.right.left = TreeNode()
H6.right.left.val = 15
H6.right.right = TreeNode()
H6.right.right.val = 7

H7 = TreeNode()
H7.val = 3
H7.left = TreeNode()
H7.left.val = 9
H7.right = TreeNode()
H7.right.val = 20
H7.right.left = TreeNode()
H7.right.left.val = 8
H7.right.right = TreeNode()
H7.right.right.val = 7

print(isSameTree(Head,Head))
print(isSameTree(Head,Head2))
print(isSameTree(Head2,Head2))
print(isSameTree(Head2,Head3))
print(isSameTree(Head4,Head4))
print(isSameTree(None,None))
print(isSameTree(H6,H7))