class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        for row in matrix :
            # print(row)
            l, r = 0, len(matrix[0])-1
            while l <= r :
                p = (l+r)// 2
                # print(row[p])
                if row[p] == target:
                    return True
                elif row[p] > target:
                    r = p -1
                else : l = p +1
        return False
        