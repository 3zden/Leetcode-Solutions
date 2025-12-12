class Solution(object):
    def summaryRanges(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        l,r = 0, 1
        poi = 0
        lista = []
        while r < len(nums):
            if nums[poi] + 1 != nums[r]:
                if poi != l :
                    lista.append(f"{nums[l]}->{nums[poi]}")
                    
                else : 
                    lista.append(f"{nums[poi]}")
                l = r
            r += 1
            poi += 1
            # if r == len(nums) -1 :

        return lista
    
solu = Solution()
print(solu.summaryRanges([0,1,2,4,5,7]))
print(solu.summaryRanges([0,2,3,4,6,8,9]))