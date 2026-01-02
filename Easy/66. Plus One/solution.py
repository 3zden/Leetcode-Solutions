class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        p = len(digits) - 1
        if digits[p] != 9:
            digits[p] += 1
        else :
            if len(digits) == 1 :
                return [1,0]
            while digits[p] == 9 and p >= 0:
                if digits[p-1] != 9:
                    digits[p] = 0
                    digits[p-1] += 1 
                    return digits
                else : 
                    if p == 1:
                        digits[p-1] = 1
                        digits.append(0)
                    digits[p] = 0      
                p -= 1      
        return digits