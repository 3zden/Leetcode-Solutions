class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dicto = {}
        for i in nums :
            if i not in dicto:
                dicto[i] = 1
            else : 
                del dicto[i] 
        return next(iter(dicto.keys()))