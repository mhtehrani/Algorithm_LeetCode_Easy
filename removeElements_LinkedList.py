"""
Remove Linked List Elements
===========================

@author: mhtehrani
November 11, 2021
https://github.com/mhtehrani

"""

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    #end
#end

def removeElements(head, val):
    if not head:
        return head
    #end
    
    node = head
    while node.val == val: #if the head is equal to val
        if node.next != None:
            node = node.next
            head = node
        else:
            return None
        #end
    #end
    
    while node.next != None:
        # print(node.val)
        if node.next.val == val:
            if node.next.next != None:
                node.next = node.next.next
            else:
                node.next = None
            #end
        else:
            node = node.next
        #end
    #end
    
    return head
#end

head = ListNode(7)
head.next = ListNode(7)
head.next.next = ListNode(7)
head.next.next.next = ListNode(7)
# head.next.next.next.next = ListNode(4)
# head.next.next.next.next.next = ListNode(5)
# head.next.next.next.next.next.next = ListNode(7)

head2 = ListNode()

hh = removeElements(head, 7)
while hh:
    print(hh.val)
    if hh.next != None:
        hh = hh.next
    else:
        break
    #end
    