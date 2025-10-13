##  32ms runtime

class Solution:
    def maximumDifference(self, nums: List[int]) -> int:
        maximum = nums[-1]
        output = 0

        for x in range(1, len(nums)+1):
            if nums[-x] > maximum:
                maximum = nums[-x]
            
            nums[-x] = maximum - nums[-x]
            output = nums[-x] if output < nums[-x] else output

        return output if output > 0 else -1