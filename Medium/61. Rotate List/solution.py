# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def rotateRight(self, head, k):
        """
        :type head: Optional[ListNode]
        :type k: int
        :rtype: Optional[ListNode]
        """
        if k == 0 or not head: return head
        stack = []
        curr = head
        while curr:
            stack.append(curr)
            curr = curr.next
        n = len(stack)
        rem = stack[n-k%n:]
        stack = stack[:n-k%n]
        out = None
        while stack:
            out, out.next = stack.pop(-1), out
        while rem:
            out, out.next = rem.pop(-1), out
        return out