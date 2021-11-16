"""
Is there a Cycle in a Linked List
=================================

@author: mhtehrani
November 05, 2021
https://github.com/mhtehrani

"""

# Definition for singly-linked list.
class ListNode:
    def __init__(self, value=0, next=None):
        self.val = value
        self.next = next

def hasCycle(head):
    if not head:
        return False
    #end
    
    node = head
    while node.next != None:
        if node.val == "Visited":
            return True
        else:
            node.val = "Visited"
            node = node.next
        #end
    #end
    
    return False
#end

H = ListNode()
H.val = 3
H.next = ListNode()
H.next.val = 2
H.next.next = ListNode()
H.next.next.val = 0
H.next.next.next = ListNode()
H.next.next.next.val = -4
H.next.next.next.next = H


print(hasCycle(H))



        