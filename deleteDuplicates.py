"""
Delete Duplicate Nodes in a Linked List
=======================================

@author: mhtehrani
October 31, 2021
https://github.com/mhtehrani

"""

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    #end
#end

def deleteDuplicates(head):
    aa = head
    while aa != None:
        print(aa.val)
        aa = aa.next
    #end
     
    dummy = head
    Node = dummy
    while Node.next != None:
        if not head:
            return head
        # print(Node.val, Node.next.val)
        if Node.val == Node.next.val:
            Node.next = Node.next.next
        elif Node.val < Node.next.val:
            Node = Node.next
        #end
    #end
    return dummy
#end

l1 = ListNode()
l1.val = 1
l1.next = ListNode()
l1.next.val = 1
l1.next.next = ListNode()
l1.next.next.val = 2
l1.next.next.next = ListNode()
l1.next.next.next.val = 3
l1.next.next.next.next = ListNode()
l1.next.next.next.next.val = 3
l1.next.next.next.next.next = None

a = deleteDuplicates(l1)
while a.next != None:
    print(a.val)
    a = a.next
#end
print(a.val)