class Solution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        dicto ={}
        out = []
        if len(nums1) > len(nums2) :
            for i in nums2 :
                if i in dicto :
                    dicto[i] += 1
                else : dicto[i] = 1
            for j in nums1:
                if j in dicto and dicto[j] != 0 :
                    out.append(j)
                    dicto[j] -= 1
                else :continue
        else :
            for i in nums1 :
                if i in dicto :
                    dicto[i] += 1
                else : dicto[i] = 1
            for j in nums2:
                if j in dicto and dicto[j] != 0 :
                    out.append(j)
                    dicto[j] -= 1
                else :continue
        return out