class Solution(object):
    def findShortestSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dicto = {}
        i = 0
        frqs = 0
        while i < len(nums):
            if nums[i] in dicto:
                dicto[nums[i]].append(i)
            else : 
                dicto[nums[i]] = [i]
            frqs = max(frqs, len(dicto[nums[i]]))
            i += 1
        minn = float('inf')
        for i in dicto.values():
            if len(i)==frqs:
                minn = min(minn,i[-1] - i[0] + 1)
            else : continue
        return minn