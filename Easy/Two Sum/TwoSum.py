class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        dict = {}
        for i in range(len(nums)):
            if dict != {} :
                s = target - nums[i]
                if s in dict :
                    return [dict[s], i]
                    break
                dict[nums[i]] = i
            dict[nums[i]] = i