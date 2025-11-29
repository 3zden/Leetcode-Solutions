class Solution(object):
    def minOperations(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        s = sum(nums)
        count = k
        numOfOpe = 0
        while count >= 0:
            if s % k == 0 :
                return numOfOpe
            else :
                s -= 1
                numOfOpe += 1
                count -=1
        return numOfOpe