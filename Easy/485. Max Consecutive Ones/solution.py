class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        maxx = 0
        streak = 0
        for v in nums:
            if v == 1:
                streak += 1
            else : 
                maxx = max(maxx,streak)
                streak = 0
        maxx = max(streak,maxx)
        return maxx

