#runtime : 4ms 

class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        output = 0
        for x in nums:
            digit = 0
            while True:
                if x == 0:
                    output = output+1 if digit%2 == 0 else output
                    break
                digit +=1
                x = x//10
        
        return output