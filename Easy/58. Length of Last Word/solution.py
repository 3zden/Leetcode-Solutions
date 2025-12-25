class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        count = 0
        i = len(s)-1
        passed = False
        while i >= 0 :
            if s[i] != " ":
                count +=1
                passed = True
            elif  passed and s[i] == " " :
                return count
            i -= 1
        return count