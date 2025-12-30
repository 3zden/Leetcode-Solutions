class Solution(object):
    def dailyTemperatures(self, temperatures):
        """
        :type temperatures: List[int]
        :rtype: List[int]
        """
        stack = [[0,temperatures[0]]]
        out = [0]*len(temperatures)
        for i, v in enumerate(temperatures):
            # print(stack[-1][1])
            while stack != [] and v > stack[-1][1]:
                out[stack[-1][0]] = i - stack[-1][0]
                stack.pop(-1)
            stack.append([i,v])
        return out
