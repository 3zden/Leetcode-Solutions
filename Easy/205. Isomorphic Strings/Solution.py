class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        dictt = {}
        sett = set()
        for i in range(len(s)):
            if s[i] in dictt :
                if dictt[s[i]] != t[i]:
                    return False
                else : continue
            else : 
                if t[i] in sett:
                    return False
                else :
                    dictt[s[i]] = t[i] 
                    sett.add(t[i])
        return True