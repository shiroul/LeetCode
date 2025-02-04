# Intuition
The idea for this solution is by put all the value in the list to dictionary, so we will get value and index in same place. after we fill the ditionary, we will subtract the target value with current value. so we will get the output value that we need, if the temp dict doesnt contain output value then we store the current value with the index to temp dict untill we found what we looking for.

# Approach
1. initialize variable
assign temp with '{}' so it make it became  dictionary

2. Loop through Enumerate List
- store index value inside variable i, and nums value inside num variable
- assign output variable by subtracting target value with current value
    - IF output value exist inside temp dict
    return index of output value inside the dict and the current index
    - ELSE add output as key value to temp dict with the value of the index

# Complexity
- Time complexity: O(1)
time complexity only O(1), becase we only travel once throgh the list

- Space complexity: O(n)
n = lenght of the dict, the worst case that we can get is if the correct answer is in the last of the list.

# Code
```python3 []
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        temp = {}
        output = 0

        for i, num in enumerate(nums):
            output = target - num

            if output in temp:
                return [temp[output] , i]

            temp[num] = i
```