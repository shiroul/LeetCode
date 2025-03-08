class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        temp = [1 if x == 'B' else 0 for x in blocks]
        
        maxSum = output = sum(temp[:k])

        for x in range(len(blocks)-k):
            maxSum = maxSum - temp[x] + temp[x+k]

            output = max(maxSum,output)
        
        return k-output