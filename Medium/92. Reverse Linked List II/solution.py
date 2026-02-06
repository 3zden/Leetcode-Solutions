# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseBetween(self, head, left, right):
        """
        :type head: Optional[ListNode]
        :type left: int
        :type right: int
        :rtype: Optional[ListNode]
        """
        stack = []
        curr = head
        while curr :
            stack.append(curr)
            curr = curr.next
        l,r = left -1, right -1
        while l < r:
            stack[l],stack[r] = stack[r], stack[l]
            l += 1
            r -= 1
        out = None
        while stack:
            out, out.next = stack.pop(-1), out
        return out
        