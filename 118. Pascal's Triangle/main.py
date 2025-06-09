class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        output = [[1], [1,1]]

        if numRows <= 2:
            return output[:numRows]

        for x in range(2, numRows):
            temp = [1]
            for y in range(1, x):
                temp.append(output[x-1][y] + output[x-1][y-1])
            temp.append(1)
            output.append(temp)
        
        return output