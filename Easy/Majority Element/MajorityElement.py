class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dicto = {}
        for i in nums :
            if i in dicto:
                dicto[i] += 1
            else: dicto[i] = 1
        for k,v in dicto.items():
            if v > len(nums)/2:
                return k
            else : continue