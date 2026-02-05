# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: bool
        """
        li = [head.val]
        curr = head
        while curr.next:
            li.append(curr.next.val)
            curr = curr.next
        l, r = 0, len(li)-1
        while l < r :
            if li[l] != li[r]:
                return False
            l += 1
            r -= 1
        return True
        