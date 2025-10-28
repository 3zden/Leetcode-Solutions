import re

class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """

        s = s.split(" ")
        s = "".join(s).lower()
        s = re.sub(r'[^a-zA-Z0-9]', '', s)
        if s == "":
            return True
        pointer = len(s) - 1
        for i in range(len(s)):
            if s[i] == s[pointer]:
                pointer -= 1
                if pointer < 0:
                    return True
            else:
                continue
        return False   
        

     