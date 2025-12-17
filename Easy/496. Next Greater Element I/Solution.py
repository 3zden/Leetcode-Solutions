class Solution(object):
    def nextGreaterElement(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        dicto = {}
        q = []
        for i, v in enumerate(nums2):
            while len(q) > 0 and v > q[-1]:
                dicto[q[-1]] = v
                q.pop(-1)
            q.append(v)
            dicto[v] = -1
        
        for k,v in enumerate(nums1):
            nums1[k] = (dicto[v])
        return nums1