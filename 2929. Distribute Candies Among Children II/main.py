#runtime : 5138ms
#beats : 8%

class Solution:
    def distributeCandies(self, n: int, limit: int) -> int:
        count = 0

        for x in range(limit+1):
            minimumYCombination = max(0, n-x-limit)
            maximumYCombination = min(limit, n-x)

            if maximumYCombination >= minimumYCombination:
                count+= (maximumYCombination - minimumYCombination +1)
        return count