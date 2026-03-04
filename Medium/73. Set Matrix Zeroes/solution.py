class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        rows = set()
        cols = set()
        for r in range(len(matrix)):
            for e in range(len(matrix[0])):
                if matrix[r][e] == 0:
                    rows.add(r)
                    cols.add(e)
        # print(rows,cols)
        for r in range(len(matrix)):
            for e in range(len(matrix[0])):
                if e in cols or r in rows:
                    matrix[r][e] = 0
        return matrix