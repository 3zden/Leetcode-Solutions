class Solution(object):
    def minLength(self, s):
        """
        :type s: str
        :rtype: int
        """
        stack = []
        for i in s :
            if not stack:
                stack.append(i)
                continue
            if (i == "B" and stack[-1] == "A") or (i == "D" and stack[-1] == "C"):
                stack.pop(-1)
            else : stack.append(i)
        return len(stack)