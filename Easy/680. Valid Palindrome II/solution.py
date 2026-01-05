class Solution(object):
    def isPalindrome(self,s):
        l, r = 0, len(s)-1
        while r >= l :
            if s[r] != s[l] :
                return False
            r -= 1
            l += 1
        return True            

    def validPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        l, r = 0, len(s)-1
        valid = True
        while r >= l :
            if s[r] == s[l] :
                r -= 1
                l += 1
            elif valid :
                if s[r-1] == s[l] and s[l+1] == s[r]:
                    return self.isPalindrome(s[l:r]) or self.isPalindrome(s[l+1:r+1])
                elif s[r-1] == s[l]:
                    r -= 1
                elif s[l+1] == s[r]:
                    l += 1
                else :return False
                valid = False
            else :
                return False
        return True