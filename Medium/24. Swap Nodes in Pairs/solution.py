# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def swapPairs(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        stack = []
        curr = head
        while curr :
            stack.append(curr)
            curr  =curr.next
        if len(stack) < 2: return head
        elif len(stack) % 2 == 1 :
            out = stack.pop(-1)
        else : out = None
        while stack:
            fs,sc = stack.pop(-1),stack.pop(-1)
            out, out.next = sc, out
            out, out.next = fs, out
        return out