class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        i = 0
        dictt = {}
        while i < len(nums) :
            if nums[i] in dictt and (i - dictt[nums[i]]) <= k:
                return True
            else : 
                dictt[nums[i]] = i
                i += 1
        return False