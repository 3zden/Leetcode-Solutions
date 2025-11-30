class Solution(object):
    def validPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        right = len(s) -1
        left = 0
        valid = True
        count = 1
        while right > left +1 :
            if s[right] == s[left] :
                print("match", s[left], s[right])
                left += 1
                right -= 1
                
            elif s[right -1] == s[left] and count == 1:
                print("here1", s[right], s[left])
                right -= 1
                count -= 1
                

            elif s[right] == s[left + 1] and validPalindrome(s[left + 1: right + 1]) and count == 1:
                print("here2", s[right], s[left])
                left += 1
                count -= 1
                
            else : 
                print("here3", s[right], s[left])
                return False

        return valid
    