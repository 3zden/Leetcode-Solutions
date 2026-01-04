class MinStack(object):

    def __init__(self):
        self.stack = []
        self.mins = []
        self.mn = float('inf')
        
    def push(self, val):
        """
        :type val: int
        :rtype: None
        """
        if val <= self.mn :
            self.mn = val
            self.mins.append(val)
        self.stack.append(val) 
        

    def pop(self):
        """
        :rtype: None
        """
        if self.stack != [] and self.stack[-1] == self.mn :
            self.mins.pop(-1)
            if self.mins != []:
                self.mn = self.mins[-1]
            else :
                self.mn = float('inf')
        self.stack.pop(-1)

        

    def top(self):
        """
        :rtype: int
        """
        if self.stack == [] : return []
        return self.stack[-1]
        

    def getMin(self):
        """
        :rtype: int
        """
        if self.mins == [] or self.mn == float('inf') : return []
        return self.mins[-1]
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()