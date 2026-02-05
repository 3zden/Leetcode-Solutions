# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        stack = []
        l, r = list1, list2
        while l or r :
            if l and r : 
                if l.val < r.val :
                    stack.append(l)
                    l = l.next
                else :
                    stack.append(r)
                    r = r.next
            elif not l:
                stack.append(r)
                r = r.next
            else :
                stack.append(l)
                l = l.next
        out = None
        while stack:
            out, out.next = stack.pop(-1),out
        return out

        