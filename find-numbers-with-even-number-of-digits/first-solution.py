#runtime : 3ms

class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        output = 0

        for x in nums:
            if len(str(x)) % 2 == 0:
        
                output+=1
        
        return output