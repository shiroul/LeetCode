##Runtime : 0ms
##beats : 100%

class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        freqDict = {}
        maximumFreq = 0
        output = 0

        for x in nums:
            freqDict[x] = freqDict.get(x, 0) + 1
            
            freq = freqDict[x]

            if freq > maximumFreq:
                maximumFreq , output = freq, freq
                continue

            if freq == maximumFreq:
                output+=freq

        return output

        

