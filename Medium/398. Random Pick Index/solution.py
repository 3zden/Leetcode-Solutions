class Solution(object):

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.nums = nums
        self.di = {}
        

    def pick(self, target):
        """
        :type target: int
        :rtype: int
        """
        if target in self.di :
            return random.choice(self.di[target])
        targets = []
        for i,v in enumerate(self.nums):
            if v == target :
                targets.append(i)
            else : continue
        self.di[target] = targets
        return random.choice(targets)