![image.png](https://assets.leetcode.com/users/images/61dc1ad4-94cd-4f69-bde1-e7954a519668_1748753886.3703303.png)

# Intuition
The problem asks us to find the number of ways to distribute `n` candies among three children (let's say they receive `x`, `y`, and `z` candies respectively) such that each child receives between 0 and `limit` candies. A naive approach using three nested loops (one for each child) would check every single combination, leading to a complexity around `O(limit^3)` or `O(n^3)`, which is too slow for typical constraints.

The key idea for optimization is to iterate through the possible number of candies for the first child (`x`). For each chosen `x`, instead of iterating through all possibilities for the second child (`y`), we can mathematically determine the valid range of candies `y` can receive. If `y` is chosen from this valid range, the number of candies for the third child (`z = n - x - y`) will automatically satisfy its constraints (`0 ≤ z ≤ limit`).

By calculating the lower and upper bounds for `y` directly, we can find the number of valid choices for `y` in constant time for each `x`. This significantly reduces the overall complexity.

# Approach
The algorithm works as follows:

### 1. Initialize a Counter:
We start with a `count` variable initialized to 0. This variable will accumulate the total number of valid ways to distribute the candies.

### 2. Iterate Through Candies for the First Child (x):
We loop `x` through all possible values it can take, which is from 0 to `limit` candies.

### 3. Determine the Valid Range for Candies for the Second Child (y):
For each value of `x`, we need to find the range of values for `y` such that:

- `0 ≤ y ≤ limit` (Constraint on `y` itself)
- And, if `z = n - x - y`, then `0 ≤ z ≤ limit` (Constraint on `z`)

Let's derive `minimumYCombination` (the minimum valid `y`) and `maximumYCombination` (the maximum valid `y`):

#### Calculating `minimumYCombination` (Lower Bound for `y`):

- `y` must be at least 0: `y ≥ 0`
- The candies for the third child, `z`, must be at most `limit`. Since `z = n - x - y`:  
  `n - x - y ≤ limit`  
  Rearranging this for `y`, we get:  
  `y ≥ n - x - limit`

To satisfy both conditions (`y ≥ 0` and `y ≥ n - x - limit`), `y` must be greater than or equal to the larger of these two expressions. Thus,  
`minimumYCombination = max(0, n - x - limit)`.

#### Calculating `maximumYCombination` (Upper Bound for `y`):

- `y` must be at most `limit`: `y ≤ limit`
- The candies for the third child, `z`, must be at least 0. Since `z = n - x - y`:  
  `n - x - y ≥ 0`  
  Rearranging this for `y`, we get:  
  `y ≤ n - x`

To satisfy both conditions (`y ≤ limit` and `y ≤ n - x`), `y` must be less than or equal to the smaller of these two expressions. Thus,  
`maximumYCombination = min(limit, n - x)`.

### 4. Count Valid Combinations for `y`:
If `maximumYCombination < minimumYCombination`, it means there are no valid values for `y` for the current `x` that satisfy all conditions.  
Otherwise (if `maximumYCombination ≥ minimumYCombination`), any integer value of `y` from `minimumYCombination` to `maximumYCombination` (inclusive) is a valid choice. The number of such valid choices for `y` is `maximumYCombination - minimumYCombination + 1`.  
We add this number to our total `count`.

### 5. Return Result:
After iterating through all possible values of `x`, the `count` variable will hold the total number of ways to distribute the `n` candies according to the rules. This count is returned.

The equations you mentioned, `Z = n - X - Y` (using `X` and `Y` for the first two children) and `0 ≤ Z ≤ limit`, are precisely the constraints used to derive the bounds for `Y`.

# Complexity

### Time Complexity: `O(n)` n = limit

### Space Complexity: `O(1)`

# Code
```python3 []
class Solution:
    def distributeCandies(self, n: int, limit: int) -> int:
        count = 0

        for x in range(limit+1):
            minimumYCombination = max(0, n-x-limit)
            maximumYCombination = min(limit, n-x)

            if maximumYCombination >= minimumYCombination:
                count+= (maximumYCombination - minimumYCombination +1)
        return count
```