# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[Optional[ListNode]]
        :rtype: Optional[ListNode]
        """
        stack = []
        for lst in lists:
            curr = lst
            while curr :
                stack.append(curr.val)
                curr = curr.next
        stack.sort()
        out = None
        while stack:
            out = ListNode(stack.pop(-1),out)
        return out
        