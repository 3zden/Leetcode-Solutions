# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def middleNode(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        if not head.next :
            return head
        curr = head
        leng = 1
        while curr :
            if curr.next:
                leng += 1
            curr = curr.next
        k = 0
        mid = head
        while k < leng // 2:
            mid = mid.next
            k +=1
        return mid