class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        di, added = {}, {}
        out = []
        for i in nums:
            if i not in di :
                di[i] = 1
            else : 
                di[i] += 1
            if di[i] > len(nums)//3 and i not in added:
                    out.append(i)
                    added[i] = 1
        return out
        