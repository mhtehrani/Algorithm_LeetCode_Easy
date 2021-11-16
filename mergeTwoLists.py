"""
Merge Two Lists
===============

@author: mhtehrani
October 27, 2021
https://github.com/mhtehrani

"""

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    #end
#end

def mergeTwoLists(l1, l2):
    dummy = ListNode(0)
    sorted  = dummy
    while l1 and l2:
        if l1.val <= l2.val:
            sorted.next = l1
            l1 = l1.next
        else:
            sorted.next = l2
            l2 = l2.next
        #end
        sorted = sorted.next
    #end
    
    if l1:
        sorted.next = l1
    elif l2:
        sorted.next = l2
    #end
    
    return dummy.next # to not report the initial "0"
#end

l1 = ListNode()
l1.val = 1
l1.next = ListNode()
l1.next.val = 2
l1.next.next = ListNode()
l1.next.next.val = 4

l2 = ListNode()
l2.val = 1
l2.next = ListNode()
l2.next.val = 3
l2.next.next = ListNode()
l2.next.next.val = 4

s = mergeTwoLists(l1, l2)

while s:
    print(s.val)
    s = s.next
#end