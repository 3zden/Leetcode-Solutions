class Solution(object):
    def findIntersectionValues(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        s1, s2 = set(nums1),set(nums2)
        ans1, ans2 = 0,0
        for i in nums1:
            if i in s2:
                ans1 += 1
            else :continue
        for j in nums2:
            if j in s1:
                ans2 += 1
            else : continue
        return [ans1,ans2]