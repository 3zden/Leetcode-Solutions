# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: Optional[ListNode]
        :type n: int
        :rtype: Optional[ListNode]
        """
        curr = head
        stack = []
        c = 0
        while curr :
            c += 1
            curr = curr.next
        k = c-n+1
        curr = head
        while curr :
            k -= 1
            if k != 0:
                stack.append(curr)
            curr = curr.next
        out = None
        while stack:
            out, out.next = stack.pop(-1), out
        return out
