#Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        head = ListNode(0)
        head1,head2,nhead= l1,l2,head
        while(head1 or head2):
            if head1 is None:
                nhead.next = head2
                head2 = head2.next
            elif head2 is None:
                nhead.next = head1
                head1 = head1.next
            elif head1.val<=head2.val:
                nhead.next = head1
                head1 = head1.next
            else:
                nhead.next = head2
                head2 = head2.next
            nhead = nhead.next
        return head.next


    def insert(self,head,node):
        pre = head
        while(pre.next):
            pre = pre.next
        pre.next = node