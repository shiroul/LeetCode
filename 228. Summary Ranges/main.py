class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        if len(nums) <= 1:
            return [str(x) for x in nums]
        temp = str(nums[0])
        output = []

        for x in range(1, len(nums)):
            if nums[x] - nums[x-1] != 1:
                if temp == str(nums[x-1]): 
                    output.append(temp)
                    temp = str(nums[x])
                else:
                    output.append(temp+f'->{nums[x-1]}')
                    temp = str(nums[x])
        if nums[-1] - nums[-2] != 1:
            output.append(temp)
        else:
            output.append(temp+f'->{str(nums[-1])}')
        
        return output