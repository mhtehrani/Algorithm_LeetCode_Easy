"""
Get the Intersection Nodes of Two Linked Lists
==============================================

@author: mhtehrani
November 06, 2021
https://github.com/mhtehrani

"""

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

def getIntersectionNode_O_n(headA, headB):
    TraverseA = [headA]
    node = headA
    while node.next != None:
        TraverseA.append(node.next)
        node = node.next
    #end
    
    node = headB
    if node in TraverseA:
        return node.val
    #end
    i = 1
    while node.next != None:
        i += 1
        if node.next in TraverseA:
            return node.next.val
        #end
        node = node.next
    #end
    
    return None
#end

def getSize(node):
    n = 0
    while node:
        n += 1
        node = node.next
    #end
    return n
#end

def getIntersectHelper(diff, longNode, shortNode):
    for i in range(diff):
        longNode = longNode.next
    #end
    
    while longNode != shortNode:
        if longNode == None and shortNode == None:
            return None
        #end
        
        longNode = longNode.next
        shortNode = shortNode.next
    #end
    
    return longNode

def getIntersectionNode_O_1(headA, headB):
    lenA = getSize(headA)
    lenB = getSize(headB)
    
    if lenA > lenB:
        return getIntersectHelper(lenA-lenB, headA, headB)
    else:
        return getIntersectHelper(lenB-lenA, headB, headA)
    #end
#end


Inters = ListNode(8)
Inters.next = ListNode(4)
Inters.next.next = ListNode(5)

headA = ListNode(4)
headA.next = ListNode(1)
# headA.next.next = Inters

headB = ListNode(5)
headB.next = ListNode(6)
headB.next.next = ListNode(1)
headB.next.next.next = Inters

print(getIntersectionNode_O_1(headA, headB))