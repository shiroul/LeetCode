def maxAscendingSum(self, nums: List[int]) -> int:
    temp = output = nums[0]

    for i in range(1, len(nums)):
        if nums[i] > nums[i-1]:
            temp += nums[i]
            output = max(temp, output)
        else:
            temp = nums[i]
    return output
        