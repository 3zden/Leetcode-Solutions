class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        dictt = {}
        dictt["largest"] = nums[0]
        for i in nums :
            if i >  1