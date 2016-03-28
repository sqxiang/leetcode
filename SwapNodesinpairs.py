# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head is None or head.next is None:
            return head
        nhead = ListNode(0)
        nhead.next = head
        p1,p2 = nhead,head
        while(p2 and p2.next):
            pre = p1
            p1 = p1.next
            p2 = p2.next
            after = p2.next
            pre.next = p2
            p2.next = p1
            p1.next = after
            p2 = after

        return nhead.next
