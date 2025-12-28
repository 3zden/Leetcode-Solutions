class Solution(object):
    def findContentChildren(self, g, s):
        """
        :type g: List[int]
        :type s: List[int]
        :rtype: int
        """
        g.sort(), s.sort()
        ch, c = 0, 0
        out = 0
        while ch < len(g) and c < len(s):
            if s[c] >= g[ch] :
                out += 1
                c += 1
                ch += 1
            else :
                c += 1
        return out 
        