# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeElements(self, head, val):
        """
        :type head: Optional[ListNode]
        :type val: int
        :rtype: Optional[ListNode]
        """
        stack = []
        curr = head
        while curr:
            if curr.val != val:
                stack.append(curr)
            curr = curr.next
        out = None   
        while stack:
            out,out.next = stack.pop(-1), out
        return out     