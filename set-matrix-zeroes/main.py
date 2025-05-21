class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        colChange = [0] * len(matrix)
        rowChange = [0] * len(matrix[0])

        for x in range(len(matrix)):
            for y in range(len(matrix[0])):
                if matrix[x][y] == 0:
                    if colChange[x] == 0:
                        colChange[x] = 1

                    if rowChange[y] == 0:
                        rowChange[y] = 1
        
        for x in range (len(colChange)):
            if colChange[x] == 0:
                continue
            for y in range(len(matrix[0])):
                matrix[x][y] = 0
        
        for y in range (len(rowChange)):
            if rowChange[y] == 0:
                continue
            for x in range(len(matrix)):
                matrix[x][y] = 0

        
