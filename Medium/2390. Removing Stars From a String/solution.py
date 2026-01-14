class NumMatrix(object):

    def __init__(self, matrix):
        """
        :type matrix: List[List[int]]
        """
        self.mtrx = [[0]*len(matrix[0])]*len(matrix)
        lis = [0]*len(matrix[0])
        for x,v in enumerate(matrix[0]):
            lis[x] = lis[x-1] + matrix[0][x]
        self.mtrx[0] = lis
        for r in range(1,len(matrix)):
            lis = [0]*len(matrix[0])
            lis[0] = matrix[r][0] + self.mtrx[r-1][0]
            for c in range(1,len(matrix[0])):
                lis[c] = matrix[r][c] + self.mtrx[r-1][c] + lis[c-1] - self.mtrx[r-1][c-1]
            self.mtrx[r] = lis

        

    def sumRegion(self, row1, col1, row2, col2):
        """
        :type row1: int
        :type col1: int
        :type row2: int
        :type col2: int
        :rtype: int
        """
        if col1 == 0 and row1 == 0:
            return self.mtrx[row2][col2]
        elif col1 == 0:
            return self.mtrx[row2][col2] - self.mtrx[row1-1][col2]
        elif row1 == 0:
            return self.mtrx[row2][col2] - self.mtrx[row2][col1-1]
        return self.mtrx[row2][col2] - self.mtrx[row1-1][col2] - self.mtrx[row2][col1-1] +self.mtrx[row1-1][col1-1]
        


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)