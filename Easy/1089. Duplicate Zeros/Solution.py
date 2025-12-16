class Solution(object):
    def duplicateZeros(self, arr):
        """
        :type arr: List[int]
        :rtype: None Do not return anything, modify arr in-place instead.
        """
        i = 0
        while i < len(arr) -1 :
            if arr[i] == 0 :
                arr [i+2:] = arr[i+1:len(arr) - 1]
                arr [i+1] = 0
                # arr [i+2:] = rem
                i += 1
            i += 1
        return arr