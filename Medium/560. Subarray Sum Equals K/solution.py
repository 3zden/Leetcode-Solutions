class Solution(object):
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        out = 0
        pr = [0]*len(nums)
        di = {}
        for i in range(len(nums)):
            pr[i] = pr[i-1] + nums[i]
            if pr[i] == k : out += 1

            if (pr[i]-k) in di:
                out += di[pr[i] - k]

            if pr[i] not in di:
                di[pr[i]] = 1
            else : di[pr[i]] += 1 
        return out