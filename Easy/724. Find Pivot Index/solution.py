class Solution(object):
    def pivotIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        pre = [0]*len(nums)
        for i, v in enumerate(nums):
            pre[i] = pre[i-1] + v
        for k,p in enumerate(pre) :
            if (k == 0 and pre[-1]-p == 0) or (k == len(nums)-1 and pre[k-1] == 0) :
                return k
            elif k != 0 and pre[k-1] == pre[-1] - p :
                return k
            else : continue
        return -1