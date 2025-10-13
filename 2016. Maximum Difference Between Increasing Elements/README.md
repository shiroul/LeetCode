# Intuition

The idea is to iterate through the list in **reverse order**, keeping track of the **maximum value** encountered so far. For each element, we calculate the **difference** between the current maximum and the element. If this difference is greater than the current best (`output`), we update it. This helps us find the **maximum difference** where the larger number comes after the smaller one.

# Approach

1. **Define variables**:
   - `maximum`: Stores the maximum value encountered while iterating in reverse.
   - `output`: Stores the maximum positive difference found so far.

2. **Iterate through the list in reverse**:
   - For each element:
     - If the current value is greater than `maximum`, update `maximum`.
     - Otherwise, compute `maximum - current_value` and update `output` if the result is larger.

3. **Return result**:
   - If `output` is still `0`, return `-1` (no increasing pair found).
   - Otherwise, return the `output`.

# Complexity

- **Time Complexity**:  
  `O(n)`  
  We iterate through the list once.

- **Space Complexity**:  
  `O(1)`  
  Only two variables are used regardless of input size.

# Code

```python
class Solution:
    def maximumDifference(self, nums: List[int]) -> int:
        maximum = nums[-1]
        output = -1

        for x in range(len(nums) - 1, -1, -1):
            if nums[x] > maximum:
                maximum = nums[x]
            else:
                output = max(output, maximum - nums[x])

        return -1 if output == 0 else output
