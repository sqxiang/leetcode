# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        nhead = ListNode(0)
        nhead.next = head
        p,t = 0,head
        while p<n:
            t = t.next
            p+=1
        pre = nhead
        while t:
            nhead,t = nhead.next,t.next
        nhead.next = nhead.next.next
        return pre.next

