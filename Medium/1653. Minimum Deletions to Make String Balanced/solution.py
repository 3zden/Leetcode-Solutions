class Solution(object):
    def minimumDeletions(self, s):
        """
        :type s: str
        :rtype: int
        """
        stack = []
        count = 0
        for c in s:
            if c == "b":
                stack.append(c)
            else : 
                if stack :
                    stack.pop(-1)
                    count += 1
        return count