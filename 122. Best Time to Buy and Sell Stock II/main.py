class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        output = 0

        for x in range(1, len(prices)):
            if prices[x] > prices[x-1]:
                output += (prices[x] - prices[x-1])
        
        return output