class Solution(object):
    def replaceElements(self, arr):
        """
        :type arr: List[int]
        :rtype: List[int]
        """
        mx = arr[-1]
        out = [-1]*len(arr)
        for i in range(len(arr)-2,-1,-1):
            out[i] = max(out[i+1],arr[i+1])
        return out

        