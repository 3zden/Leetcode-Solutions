class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        si = [x for x in s]
        se = set(['a', 'e', 'i', 'o', 'u'])
        l,r = 0, len(s)-1
        while r > l :
            if si[l].lower() in se and si[r].lower() in se :
                si[l], si[r] = si[r], si[l]
                l, r = l+1, r-1
            elif s[l].lower() in se and s[r].lower() not in se :
                r -= 1
            elif  s[l].lower() not in se and s[r].lower() in se :
                l += 1
            else : 
                l += 1
                r -= 1   
        return "".join(si)