class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        rightPointer = len(numbers)-1
        leftPointer = 0
        while (leftPointer < rightPointer):
            currentSum = numbers[rightPointer] + numbers[leftPointer]
            if currentSum == target:
                return [leftPointer+1,rightPointer+1]
            elif currentSum < target :
                leftPointer += 1
            else :
                rightPointer -= 1