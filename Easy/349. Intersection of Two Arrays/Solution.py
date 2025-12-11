class Solution(object):
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        lista = []
        if len(nums1) > len(nums2):
            sett = set(nums1)
            for i in nums2:
                if i in sett and i not in lista :
                    lista.append(i)
        else : 
            sett = set(nums2)
            for i in nums1:
                if i in sett and i not in lista :
                    lista.append(i)

        return lista