# Intuition
the idea is to store value of consecutive odd number to some variable, give it 0 for initiate value then increment it every time we had odd number but set the value to 0 every time we had even number. then return `True` when the value reach 3 or return `False` when the velue never reach 3

# Approach
- Define Variable
Declare variable consecutieve with initial value of 0

- Iterate
Loop through array and check if it is odd? using `x % 2 =! 0` if `True` then add consecutive value by `1`, but if `False` set the value to be `0`

- Return value
return `True` if the value of consecutive reach 3 or return `False` when the value never reach 3 when loop is finish

# Complexity
- Time complexity: O(n)
n = length of array

- Space complexity: O(1)
only need 1 space for consecutive variable

# Code
```python3 []
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
```