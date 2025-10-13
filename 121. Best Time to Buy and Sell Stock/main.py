class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maximum = 0
        output = 0

        for x in range(len(prices)-1, -1, -1):
            if prices[x] > maximum:
                maximum = prices[x]
            else:
                output = max(output, maximum - prices[x])
        
        return output