##Runtime : 2ms
##beats : 39.47%

class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        frequencyDict = {}
        maximumFrequency = 1

        for x in nums:
            if x not in frequencyDict:
                frequencyDict[x] = 1
                continue
            
            frequencyDict[x]+=1

            if frequencyDict[x] > maximumFrequency:
                maximumFrequency = frequencyDict[x]
        
        output = 0

        for x in frequencyDict:
            if frequencyDict[x] == maximumFrequency:
                output+=maximumFrequency
        
        return output

        

