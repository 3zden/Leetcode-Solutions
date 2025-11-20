class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        dict = {}
        for i in range(len(nums)) :
            if nums[i] in dict :
                return True
            dict[nums[i]] = 1
        return False