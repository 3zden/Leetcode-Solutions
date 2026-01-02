class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        p = min([len(st) for st in strs])
        while p >= 0:
            curr = strs[0][0:p]
            for i, st in enumerate(strs):
                if st[0:p] != curr:
                    break
                elif i == len(strs) -1:
                    return curr 
            p -= 1
        