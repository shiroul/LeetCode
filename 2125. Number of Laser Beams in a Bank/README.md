# Intuition
The idea is to calculate the number of laser beams between security devices in each row.  
Each `'1'` in a row represents a device that can send a beam to devices in other rows (as long as there are no empty rows between them).  
To find the total number of beams, we multiply the number of devices in the current non-empty row by the number of devices in the previous non-empty row, then add this to our total.  
We skip any rows that contain no devices (no `'1'`s). For the very first non-empty row, we multiply by `0` since there’s no previous row with devices.

# Approach
1. Initialize two variables:
    - `ans` to store the total number of beams.
    - `prev` to keep track the number of previous devices
2. Iterate through row in `bank`
    - count the number of device in current row and store the value to `count`
    - if `count > 0` (there is device in current row)
        - add `count * prev` to `ans` value
        - update `prev` value with `count` value to keep track each previous device count
3. return 'ans' as an answer 

# Complexity
- Time complexity: $O(m\cdot n)$
    - `m` = length in each row
    - `n` = number of rows
    we only iterate once but need to count `'1'` in every row

<!-- Add your time complexity here, e.g. $$O(n)$$ -->

- Space complexity:$O(1)$
no need extra space other than `ans`, `prev`, and `count` variable
<!-- Add your space complexity here, e.g. $$O(n)$$ -->

# Code
```python3 []
class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:
        ans = 0
        prev = 0

        for row in bank:
            count = row.count('1')
            if count > 0:
                ans = ans + ( count * prev )
                prev = count

        return ans
```