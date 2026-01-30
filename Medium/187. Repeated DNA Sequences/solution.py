class Solution(object):
    def findRepeatedDnaSequences(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        l, r = 0, 10
        if len(s) < 10: return []
        out = {}
        se = set()
        while r <= len(s):
            if s[l:r] in se :
                out[s[l:r]] = 1
            else :
                se.add(s[l:r]) 
            l += 1
            r += 1
        return out.keys()
        