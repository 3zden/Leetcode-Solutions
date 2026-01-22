class Solution(object):
    def intersection(self, nums):
        """
        :type nums: List[List[int]]
        :rtype: List[int]
        """
        out = set(nums[0])
        for num in nums[1:]:
            out = out & set(num)
        return sorted(list(out))

        
