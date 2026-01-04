class Solution(object):
    def calPoints(self, operations):
        """
        :type operations: List[str]
        :rtype: int
        """
        stack = []
        score = 0
        for i in operations:
            if i == "+" :
                if len(stack) >= 2:
                    stack.append(stack[-1]+stack[-2])
            elif i == "C":
                stack.pop(-1)
            elif i == "D":
                stack.append(stack[-1]*2)
            else :
                stack.append(int(i))
        return sum(stack)
        
