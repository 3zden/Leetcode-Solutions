# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        if not head or not head.next : return head
        stack = [head]
        prev, curr = head, head.next
        while curr:
            if curr.val != prev.val:
                prev = curr
                stack.append(curr)
            curr = curr.next
        out = None
        while stack:
            out, out.next = stack.pop(-1), out
        return out
    