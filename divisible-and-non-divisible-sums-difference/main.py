class Solution:
    def differenceOfSums(self, n: int, m: int) -> int:
        output = [0,0]

        for x in range(1, n+1):
            if x % m == 0:
                output[1]+=x
            else:
                output[0]+=x
        
        return output[0] - output[1]