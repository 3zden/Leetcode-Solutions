class Solution(object):
    def repeatedNTimes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dicto = {}
        for i in nums:
            if i not in dicto:
                dicto[i] = 1
            else : dicto[i] += 1
            if dicto[i] == len(nums)/2:
                return i
            