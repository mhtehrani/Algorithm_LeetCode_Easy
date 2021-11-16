"""
Reverse Linked List
===================

@author: mhtehrani
November 11, 2021
https://github.com/mhtehrani

"""

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def reverseList(head):
    values = []
    
    if not head:
        return None
    #end
    
    node = head
    while True:
        values.append(node.val)
        if node.next != None:
            node = node.next
        else:
            break
        #end
    #end
    
    values = values[::-1]
    head_new = ListNode(values[0])
    node = head_new
    for i in range(1,len(values)):
        node.next = ListNode(values[i])
        node = node.next
    #end
    
    return head_new
#end

head = ListNode(1)
head.next = ListNode(2)
# head.next.next = ListNode(3)
# head.next.next.next = ListNode(4)
# head.next.next.next.next = ListNode(5)
# head.next.next.next.next.next = ListNode(6)
# head.next.next.next.next.next.next = ListNode(7)

hh = reverseList(head)
while hh:
    print(hh.val)
    if hh.next != None:
        hh = hh.next
    else:
        break
    #end