## Runtime : 0ms
## beats : 100%

class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        
        output = numBottles

        while numBottles >= numExchange:
            
            exchange = numBottles // numExchange
            numBottles = exchange + numBottles%numExchange
            output += exchange

        return output

            
