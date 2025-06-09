class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        maxi = [float('-inf')] * 3
        for x in nums:
            if x > maxi[0]:
                maxi[0] , maxi[1], maxi[2] = x , maxi[0], maxi[1]
            elif x > maxi[1] and x != maxi[0]:
                maxi[1] , maxi[2] = x, maxi[1]
            elif x > maxi[2] and x < maxi[1]:
                maxi[2] = x
        
        print(maxi)
        return maxi[0] if maxi[2] == float('-inf') else maxi[2]

            