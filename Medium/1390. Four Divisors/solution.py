class Solution(object):
    def sumFourDivisors(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        out = 0
        dicto = {}
        for i in nums:
            c = int(i ** 0.5)
            if c*c == i:
                continue
            else : 
                if i in dicto:
                    out += dicto[i]
                    continue
                j, k = 1, 1
                add, found = 0, False
                while j <= c :
                    if j == k:
                        pass
                    elif i%j == 0 :
                        k = i / j
                        if not found:
                            found = True
                            add += i + j + 1 + i /j
                        else : 
                            add = 0
                            break
                    j+= 1
                out += add 
                if add != 0:
                    dicto[i] = add
        return out
