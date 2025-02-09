# Intuition
return anything below zero as False, becase anything below zero had  negative and it will count as non palindrome number, after that just convert x value to string so it more easy to reverse the value and then cast it back to integer value. finally just comapre the reverse number with the x value so if it have same value, it count as palindrome number

# Approach
1. any number below zero, return it with 'False'
2. cast the input value to bacame string value
3. use slicing to make it reversed (string[::-1])
4. cast it back to integer value
5. compare the input with reversed value
6. return true if both value have same value

# Complexity
- Time complexity:O(n)
n = the lenght of the input

- Space complexity: O(n)
n = the lenght of the input

# Code
```python3 []
class Solution:
    def isPalindrome(self, x: int) -> bool:

        if x < 0:
            return False
        return x == int((str(x))[::-1])
```