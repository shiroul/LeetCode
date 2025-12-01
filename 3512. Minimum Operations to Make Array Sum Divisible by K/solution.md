# Intuition

To find the result, we only need the sum of all elements in the array and then take that sum modulo `k`. Therefore, the idea is straightforward: traverse the array, accumulate the total sum, and finally compute `total % k`.

# Approach

1. Initialize a variable `total` to store the cumulative sum of the array.
2. Traverse through the array, adding each element to `total`.
3. Return `total % k` as the final answer.

# Complexity

* **Time Complexity:**
  **O(n)**, where *n* is the length of the array, since we traverse it once.

* **Space Complexity:**
  **O(1)**, because we only use a constant amount of extra space.

# Code

```python
class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        total = 0
        
        for x in nums:
            total += x
        
        return total % k
```