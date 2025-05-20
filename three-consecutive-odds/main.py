class Solution:
    def threeConsecutiveOdds(self, arr: List[int]) -> bool:
        consecutive = 0
        for x in arr:
            if x % 2 != 0:
                consecutive += 1
                if consecutive == 3:
                    return True
            else:
                consecutive = 0
        return False