class Solution:
    def countSubarrays(self, nums: List[int]) -> int:
        output = 0
        for x in range(len(nums)-2):
            if (nums[x] + nums[x+2])*2 == nums[x+1]:
                output+=1
        
        return output